
from transformers import Trainer, AutoModelForSequenceClassification
from process_twarc.util import  load_dict
from process_twarc.train.util import  init_run, complete_trial, launch_study, print_run_init


def run_study(
    data_dir:str,
    path_to_config: str,
    path_to_storage: str,
    preprocessed_data: bool=False,
    group: str="",
    n_trials: int=100,
    should_prune: bool=False,
):
    
    def objective(trial):
        parameters, data_collator, model, optimizers, trial_checkpoint, trial_complete, training_args, compute_metrics, callbacks = init_run(
            trial, 
            config,
            train_dataset,
            AutoModelForSequenceClassification,
            tokenizer,
            group=group,
            should_prune=should_prune
            )

        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
            optimizers=optimizers,
            compute_metrics=compute_metrics,
            callbacks=callbacks
        )

        print_run_init(model, config, parameters, trial_checkpoint)

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
    tokenizer, train_dataset, eval_dataset, test_dataset, study= launch_study(
        config,
        path_to_storage,
        data_dir,
        preprocessed_data,
        group=group
    )
    study.optimize(objective, n_trials=n_trials)