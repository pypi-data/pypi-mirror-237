
from transformers import Trainer, AutoModelForSequenceClassification, DataCollatorWithPadding
from process_twarc.util import  load_dict
from process_twarc.train.util import  init_run, get_optimizers, get_sampler, load_datasets, configure_training_args, get_callbacks, complete_trial, compute_accuracy_with_hard_labels, compute_accuracy_with_soft_labels
import optuna


def run_study(
    data_dir:str,
    path_to_config: str,
    path_to_storage: str,
    group: str="",
    n_trials: int=100,
    should_prune: bool=False,
):

    
    def objective(trial):
        config = load_dict(path_to_config)
        parameters, tokenizer, model, trial_checkpoint, trial_complete, training_args = init_run(
            trial, 
            config, 
            AutoModelForSequenceClassification, 
            group=group
            )

        train_dataset, eval_dataset, test_dataset = load_datasets(
            data_dir,
            label_column=parameters["label_column"],
            tokenizer=tokenizer
            )
        
        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
        optimizers = get_optimizers(model, parameters, train_dataset)

        callbacks = get_callbacks(
            parameters, 
            trial=trial, 
            should_prune=should_prune
            )
        training_args = configure_training_args(parameters, trial_checkpoint)

        compute_accuracy = compute_accuracy_with_hard_labels if parameters["label_type"] == "hard" else compute_accuracy_with_soft_labels

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

        trainer.train()

        results = complete_trial(
            trainer,
            test_dataset,
            parameters,
            trial_checkpoint,
            trial_complete
        )
        return results

    config = load_dict(path_to_config)
    print(config.keys())
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