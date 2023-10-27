from transformers import TrainerCallback, get_constant_schedule_with_warmup, get_linear_schedule_with_warmup, get_cosine_schedule_with_warmup, get_cosine_with_hard_restarts_schedule_with_warmup, DataCollatorWithPadding, DataCollatorForLanguageModeling, TrainingArguments, EarlyStoppingCallback, AutoModelForMaskedLM, AutoModelForSequenceClassification
from process_twarc.util import load_dataset, suggest_parameter, load_dict, load_tokenizer
import torch
from torch.optim import AdamW
import wandb
import optuna
from ntpath import basename
import evaluate
import numpy as np
import os
import shutil


class OptunaCallback(TrainerCallback):
    def __init__(self, trial, should_prune):
        self.trial = trial
        self.should_prune = should_prune

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        eval_loss = metrics.get("eval_loss")
        self.trial.report(eval_loss, step=state.global_step)
        if self.should_prune and self.trial.should_prune():
            raise optuna.TrialPruned()
        
class StopCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, logs=None, **kwargs):
        control.should_training_stop = True
        control.should_save = True

def get_compute_metrics(parameters):
    argmax_ = lambda x: np.argmax(x, axis=1)

    metrics = [parameters["metric_for_best_trial"], parameters["metric_for_best_model"]]
    if any([metric in ["accuracy", "eval_accuracy"] for metric in metrics]):

    
        def compute_accuracy(eval_pred):
            accuracy = evaluate.load("accuracy")
            predictions, labels = eval_pred
            if parameters["label_type"] == "hard":  
                predictions = argmax_(predictions)
            elif parameters["label_type"] == "soft":
                predictions, labels = argmax_(predictions), argmax_(labels)
            return accuracy.compute(predictions=predictions, references=labels)
        return compute_accuracy

def load_datasets(
        data_dir: str,
        preprocessed_data: bool=False,
        label_column: str=None,
        tokenizer: object=None):
    
    def load_(split, label_column: str=""):
        path = os.path.join(data_dir, f"{split}.parquet")
        if preprocessed_data:
            dataset = load_dataset(path, output_type="Dataset")
        else:
            columns = ["text"]
            if label_column:
                columns.append(label_column)
            dataset = load_dataset(path, output_type="Dataset", columns=columns)
            if tokenizer:
                dataset = dataset.map(lambda example: tokenizer(example["text"]), batched=True)
            if label_column:
                dataset = dataset.rename_column(
                    original_column_name=label_column,
                    new_column_name= "label")
        return dataset

    train_dataset = load_("train", label_column)
    eval_dataset = load_("validation", label_column)
    test_dataset = load_("development", label_column)

    return train_dataset, eval_dataset, test_dataset

def get_study_name(config, group: str=None):
    if group:
        study_name = group
    else:
        study_name = config["fixed_parameters"]["group"]
    return study_name

def get_sampler(config):
    search_type = config["variable_parameters"]["search_type"]
    if search_type == "TPE":
        sampler = optuna.samplers.TPESampler()
    if search_type == "random":
        sampler = optuna.samplers.RandomSampler()
    if search_type == "grid":
        search_field = {k:v for k,v in zip(
            config["variable_parameters"]["search_field"].keys(),
            [value["choices"] for value in config["variable_parameters"]["search_field"].values()]
        )}
        sampler = optuna.samplers.GridSampler(search_field)
    return sampler

def get_model(model_class, parameters, tokenizer):
    if model_class == AutoModelForSequenceClassification:
        model = model_class.from_pretrained(
            parameters["path_to_model"],
            num_labels=parameters["num_labels"],
            id2label=parameters["id2label"],
            label2id=parameters["label2id"]
        )
        collator_class = DataCollatorWithPadding

    elif model_class == AutoModelForMaskedLM:
        model = model_class.from_pretrained(
            parameters["path_to_model"]
            )
        collator_class = DataCollatorForLanguageModeling

    data_collator = collator_class(tokenizer=tokenizer)
    return model, data_collator


def get_optimizer(model, parameters, optimizer_state: str=None):
    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    optimizer = AdamW(
        params=model.parameters(),
        lr=get("learning_rate"),
        betas = (get("adam_beta1"), get("adam_beta2")),
        eps = get("adam_epsilon"),
        weight_decay = get("weight_decay")
    )
    
    if optimizer_state:
        optimizer.load_state_dict(optimizer_state)

    return optimizer


def get_scheduler(train_dataset, parameters, optimizer, scheduler_state: str=None):

    get = lambda parameter, default: parameters[parameter] if parameter in parameters.keys() else default

    lr_scheduler_type = get("lr_scheduler_type", "constant")
    batch_size = get("per_device_train_batch_size", 15)
    num_train_epochs = get("num_train_epochs", 1)
    num_cycles = get("num_cycles", 0.5)
    num_restarts = get("num_restarts", 0)
    num_warmup_steps = get("num_warmup_steps", 0)

    num_training_steps = len(train_dataset) // batch_size * num_train_epochs

    if lr_scheduler_type == "constant":
        scheduler = get_constant_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=num_warmup_steps
        )
    if lr_scheduler_type == "linear":
        scheduler = get_linear_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps= num_training_steps
        )
    
    if lr_scheduler_type == "cosine":
        scheduler = get_cosine_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps= num_training_steps,
            num_cycles=num_cycles
        )
    if lr_scheduler_type == "cosine_with_restarts":
        scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps= num_training_steps,
            num_cycles=num_restarts
        )
    if scheduler_state:
        scheduler.load_state_dict(scheduler_state)

    return scheduler

def get_optimizers(model, parameters, train_dataset, optimizer_state: str=None, scheduler_state: str=None):
    optimizer = get_optimizer(model, parameters, optimizer_state)
    scheduler = get_scheduler(train_dataset, parameters, optimizer, scheduler_state)
    return optimizer, scheduler

def get_callbacks(parameters, pause_on_epoch: bool=False, trial=None, should_prune: bool=False, current_epoch: float=0.0):
    choices = parameters["callbacks"]

    callbacks = []
    if "early_stopping" in choices:
        patience = parameters["patience"]
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=patience))
        print(f"EarlyStopping enabled. {patience=}")
    
    if "optuna" in choices:
        callbacks.append(OptunaCallback(trial, should_prune=should_prune))
        print(f"Optuna logging enabled. {should_prune=}")

    if pause_on_epoch:
        pause_epoch = int(current_epoch) + 1
        if pause_epoch< parameters["num_train_epochs"]:
            callbacks.append(StopCallback())
            print(f"Training will pause when epoch = {pause_epoch}.")
        else:
            print("Training will run to completion.")
    return callbacks


def configure_dropout(model, config, parameters):
    dropout_parameters = [key for key in parameters.keys() if "dropout" in key]
    if not dropout_parameters:
        return model, config, parameters
    else:
        get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
        def update(model, name, value): 
            model.config.update({name: value})
            parameters[name] = value
            return model, config, parameters

        for dropout in ["hidden_dropout_prob", "attention_probs_dropout_prob", "classifier_dropout"]:
            model, config, parameters = update(model, dropout, get(dropout))

        listify = lambda parameter: parameter if type(parameter) == list else [parameter]
        if "dropout_type" in parameters.keys():
            if parameters["dropout_type"]:
                label2choice = config["variable_parameters"]["search_field"]["dropout_type"]["label2choice"]
                choice = listify(label2choice[get("dropout_type")])
                if "hidden" in choice:
                    model, config, parameters = update(model, "hidden_dropout_prob", get("dropout_prob"))
                if "attention" in choice:
                    model, config, parameters = update(model, "attention_probs_dropout_prob", get("dropout_prob"))
                if "classifier" in choice:
                    model, config, parameters = update(model, "classifier_dropout", get("dropout_prob"))
                
            else:
                model, config, parameters = update(model, "dropout_prob", None)
    return model, config, parameters


def configure_training_args(
        parameters,
        trial_checkpoint
):
    if "interval" in parameters.keys():
        evaluation_strategy = save_strategy = "steps"
        eval_steps = save_steps = 1 / parameters["interval"] / parameters["num_train_epochs"]
    else:
        evaluation_strategy = save_strategy = "epoch"
        eval_steps = save_steps = 1

    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    training_args = TrainingArguments(
        adam_beta1=get("adam_beta1"),
        adam_beta2=get("adam_beta2"),
        adam_epsilon=get("adam_epsilon"),
        eval_steps=eval_steps,
        evaluation_strategy=evaluation_strategy,
        logging_steps=get("logging_steps"),
        learning_rate=get("learning_rate"),
        load_best_model_at_end=get("load_best_model_at_end"),
        lr_scheduler_type=get("lr_scheduler_type"),
        metric_for_best_model=get("metric_for_best_model"),
        num_train_epochs=get("num_train_epochs"),
        output_dir=trial_checkpoint,
        per_device_train_batch_size=get("per_device_train_batch_size"),
        per_device_eval_batch_size=get("per_device_eval_batch_size"),
        push_to_hub=get("push_to_hub"),
        report_to=get("report_to"),
        save_strategy=save_strategy,
        save_steps=save_steps,
        save_total_limit=get("patience") if get("patience") != 1 else 2,
        warmup_steps=get("num_warmup_steps"),
        weight_decay=get("weight_decay")
        )

    return training_args

def init_parameters(trial, config, override_parameters={}, group: str=None):
    fixed_parameters = config["fixed_parameters"]
    if group:
        group_parameters = config["group_parameters"][group]
        group_parameters["group"] = group
    else:
        group_parameters = {}


    search_field = config["variable_parameters"]["search_field"]
    
    suggest = lambda variable: suggest_parameter(trial, search_field, variable)
    variable_parameters = {variable: suggest(variable) for variable in search_field.keys()}

    parameters = {**fixed_parameters, **group_parameters, **variable_parameters, **override_parameters}
    return parameters

def print_parameters(config, parameters):
    
    print("\nFixed Params:")
    for key, value in config["fixed_parameters"].items():
        print(f"{key}: {value}")

    if "group_parameters" in config.keys():
        print("\nGroup Params:")
        groups = list(config["group_parameters"].keys())
        for key in config["group_parameters"][groups[0]].keys():
            print(f"{key}: {parameters[key]}")

    print("\nVariable Params:")
    for key in config["variable_parameters"]["search_field"].keys():
        if key in parameters.keys():
            print(f"{key}: {parameters[key]}")
    return

def print_run_init(model, config, parameters, trial_checkpoint, reinit: bool=False):
    print("\n", model.config)
    print_parameters(config, parameters)

    if not reinit:
        print(f"Beginning {basename(trial_checkpoint)}. . .")

    else:
        print(f"Resuming {basename(trial_checkpoint)}. . .")
    return
     

def init_run(
        trial, 
        config, 
        train_dataset,
        model_class,
        tokenizer,
        group: str="", 
        override_parameters: dict={}, 
        pause_on_epoch: bool=False, 
        should_prune: bool=False):
    
    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")
    parameters = init_parameters(trial, config, override_parameters=override_parameters, group=group)
    model, data_collator = get_model(model_class, parameters, tokenizer)
    model, config, parameters = configure_dropout(model, config, parameters)
    model.to(device)

    optimizers = get_optimizers(model, parameters, train_dataset)

    join = lambda parent, child: os.path.join(parent, child)
    trial_number = str(trial.number+1).zfill(3)
    
    name = f"{parameters['group']}/trial-{trial_number}"
    path = f"{parameters['project']}/{name}"

    trial_checkpoint = join(parameters["checkpoint_dir"], path)
    trial_complete = join(parameters["completed_dir"], path)

    training_args = configure_training_args(parameters, trial_checkpoint)
    compute_metrics = get_compute_metrics(parameters)

    callbacks = get_callbacks(
        parameters, 
        pause_on_epoch=pause_on_epoch,
        trial=trial,
        should_prune=should_prune)

    if parameters["report_to"] == "wandb":
        os.makedirs(trial_checkpoint, exist_ok=True)
        wandb.init(
            project=parameters["project"],
            dir=trial_checkpoint,
            group =parameters["group"],
            entity=parameters["entity"],
            name=name,
            resume="allow",
            config=parameters,
            reinit=True
        )
    
    return parameters, data_collator, model, optimizers, trial_checkpoint, trial_complete, training_args, compute_metrics, callbacks

def get_last_checkpoint(trial_checkpoint: str):

    checkpoints = [os.path.join(trial_checkpoint, checkpoint) for checkpoint in os.listdir(trial_checkpoint) if os.path.isdir(os.path.join(trial_checkpoint, checkpoint))]
    return max(checkpoints, key=os.path.getctime)

def retrieve_parameters(trial_checkpoint, config, model_class):
    last_checkpoint = get_last_checkpoint(trial_checkpoint)
    get = lambda target: os.path.join(last_checkpoint, target)
    training_args = torch.load(get("training_args.bin"))
    training_args_dict = {k:v for k,v in training_args.__dict__.items() if k != "callbacks"}

    model_config = load_dict(get("config.json"))
    parameters = {**training_args_dict, **model_config, **config["fixed_parameters"]}
    tokenizer = load_tokenizer(parameters["path_to_tokenizer"], print_details=False)

    model, data_collator = get_model(model_class, parameters, tokenizer)
    model.config.update(model_config)
    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")
    model.to(device)
    return last_checkpoint, training_args, parameters, tokenizer, model, data_collator

def reinit_run(
        trial_checkpoint, 
        config, 
        model_class,
        data_dir,
        group = "",
        preprocessed_data: bool=True,
        pause_on_epoch: bool=False
        ):

    last_checkpoint, training_args, parameters, tokenizer, model, data_collator = retrieve_parameters(
        trial_checkpoint, 
        config,
        model_class)
    
    train_dataset, eval_dataset, test_dataset = load_datasets(
        data_dir,
        preprocessed_data=preprocessed_data,
        label_column=parameters["label_column"] if "label_column" in parameters.keys() else "",
        tokenizer=tokenizer if not preprocessed_data else None
        )   
    
    if not group:
        group = parameters["group"]
        trial_name = basename(trial_checkpoint)
    trial_complete = os.path.join(parameters["completed_dir"], f"{group}/{trial_name}")
    
    get = lambda target: os.path.join(last_checkpoint, target)
    optimizers = get_optimizers(
        model,
        parameters,
        train_dataset,
        optimizer_state = torch.load(get("optimizer.pt")),
        scheduler_state = torch.load(get("scheduler.pt"))
        )
    
    trainer_state = load_dict(
        get("trainer_state.json"))
    current_epoch = trainer_state["epoch"]

    callbacks = get_callbacks(
        parameters,
        pause_on_epoch=pause_on_epoch,
        current_epoch=current_epoch
    )
    if parameters["report_to"] == "wandb":
        wandb_dir = os.path.join(trial_checkpoint, "wandb/latest-run")
        name = basename(os.path.realpath(wandb_dir))
        wandb_run_id = name.split("-")[-1]

        wandb.init(
            project= parameters["project"],
            id=wandb_run_id,
            resume="must"
            )
        
    return (
        last_checkpoint,
        training_args,
        parameters,
        tokenizer,
        model,
        data_collator,
        train_dataset,
        eval_dataset,
        test_dataset,
        trial_complete,
        optimizers,
        callbacks
    )

def check_if_complete(trainer, parameters):
    current_epoch = trainer.state.epoch
    if current_epoch%1 != 0:
        print("EarlyStoppingCallback triggered.")
        complete = True
    elif current_epoch == parameters["num_train_epochs"]:
        print("Training complete.")
        complete = True
    else:
        complete = False
        print(f"Training paused. {current_epoch=}.")
    return complete

def complete_trial (
        trainer, 
        test_dataset, 
        parameters, 
        trial_checkpoint, 
        trial_complete
        ):
    
    results = trainer.evaluate(test_dataset)
    print("\nResults:", results)
    trainer.save_model(trial_complete)
    if parameters["report_to"] == "wandb":
        wandb.log(results)
        wandb.finish()
        #move wandb directory to completed directory
        wandb_dir = os.path.join(trial_checkpoint, "wandb")
        shutil.move(wandb_dir, trial_complete)
    #deletes the trial directory
    shutil.rmtree(trial_checkpoint)
    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    if get("metric_for_best_trial"):
        trial_value = results[get("metric_for_best_trial")]
    elif get("metric_for_best_model"):
        trial_value = results[get("metric_for_best_model")]
    else:
        trial_value = results["eval_loss"] 
    return trial_value

def launch_study(
        config, 
        path_to_storage, 
        data_dir, 
        preprocessed_data,  
        group: str=""):

    if group:
        parameters = {**config["fixed_parameters"], **config["group_parameters"][group], **{"group": group}}
    else:
        parameters = config["fixed_parameters"]
    
    if parameters["metric_for_best_trial"] in ["accuracy", "eval_accuracy"]:
        direction = "maximize"

    elif parameters["metric_for_best_trial"] in ["loss", "eval_loss"]:
        direction = "minimize"

    tokenizer = load_tokenizer(parameters["path_to_tokenizer"], print_details=False)

    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    train_dataset, eval_dataset, test_dataset = load_datasets(
        data_dir,
        preprocessed_data=preprocessed_data,
        label_column = get("label_column"),
        tokenizer=tokenizer
        )

    study = optuna.create_study(
        storage=path_to_storage,
        sampler=get_sampler(config),
        study_name=parameters["group"],
        direction=direction,
        load_if_exists=True,
        )
    
    return tokenizer, train_dataset, eval_dataset, test_dataset, study