
from transformers import Trainer, AutoModelForSequenceClassification, DataCollatorWithPadding
from process_twarc.util import  load_dict, load_tokenizer
from process_twarc.train.util import  init_run, compute_accuracy, get_optimizers, get_sampler, load_datasets, configure_training_args, get_callbacks, print_parameters
from ntpath import basename
import wandb
import optuna
import shutil

def run_study(
    data_dir:str,
    path_to_config: str,
    path_to_storage: str,
    group: str="",
    n_trials: int=100,
    should_prune: bool=False,
    print_details: bool=True
):

    config = load_dict(path_to_config)
    def objective(trial):

        parameters, trial_checkpoint, trial_complete, training_args, model = init_run(trial, config, AutoModelForSequenceClassification, group=group)
        tokenizer = load_tokenizer(parameters["path_to_tokenizer"], print_details=print_details)
        train_dataset, eval_dataset, test_dataset = load_datasets(
            data_dir,
            label_column=parameters["label_column"], 
            tokenizer=tokenizer)
        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
        optimizers = get_optimizers(model, parameters, train_dataset)
        callbacks = get_callbacks(
            parameters, 
            trial=trial, 
            should_prune=should_prune)
        training_args = configure_training_args(parameters, trial_checkpoint)

        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
            optimizers=optimizers,
            compute_metrics=compute_accuracy,
            callbacks=callbacks
        )

        print_parameters(config, parameters)
        
        print(f"\nStarting {basename(trial_checkpoint)}. . .")
        trainer.train()
        results = trainer.evaluate(test_dataset)
        print("\nResults:", results)
        if parameters["report_to"] == "wandb":
            wandb.log(results)
        trainer.save_model(trial_complete)
        #deletes the trial directory
        shutil.rmtree(trial_checkpoint)
        trial_value = results["eval_accuracy"]
        return trial_value
    
    if group:
        study_name = group
    else:
        study_name = config["fixed_parameters"]["group"]
    study = optuna.create_study(
        storage=path_to_storage,
        sampler=get_sampler(config),
        study_name=study_name,
        direction="maximize",
        load_if_exists=True,
        )
    study.optimize(objective, n_trials=n_trials)