
from transformers import Trainer, AutoModelForMaskedLM
from process_twarc.util import  load_dict
from process_twarc.util import load_datasets, init_run, reinit_run, check_if_complete, complete_trial, launch_study, print_run_init

def initiate_trial(
    data_dir:str,
    path_to_config: str,
    path_to_storage: str,
    override_parameters: dict={},
    group: str="",
    preprocessed_data: bool=True,
    pause_on_epoch: bool=False,
    should_prune: bool=False,
):

    def objective(trial):

        config = load_dict(path_to_config)

        parameters, data_collator, model, optimizers, trial_checkpoint, trial_complete, training_args, compute_metrics, callbacks = init_run(
            trial, 
            config, 
            train_dataset,
            AutoModelForMaskedLM,
            tokenizer,
            group = group, 
            override_parameters = override_parameters, 
            pause_on_epoch = pause_on_epoch, 
            should_prune = should_prune
            )
        
   
        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
            compute_metrics=compute_metrics,
            optimizers=optimizers,
            callbacks=callbacks
        )

        print_run_init(model, config, parameters, trial_checkpoint)
        trainer.train()
        complete = check_if_complete(trainer, parameters)

        if complete:
            trial_value = complete_trial(trainer, test_dataset, parameters, trial_checkpoint, trial_complete)
        
        else:
            trial_value = 1
        
        return trial_value
    
    config = load_dict(path_to_config)
    tokenizer, train_dataset, eval_dataset, test_dataset, study = launch_study(
        config,
        path_to_storage,
        data_dir,
        preprocessed_data,
        group=group
    )
    study.optimize(objective, n_trials=1)


def resume_trial(
    data_dir:str,
    path_to_config: str,
    trial_checkpoint: str,
    preprocessed_data: bool=True,
    pause_on_epoch: bool=False,
    group: str="",
):
    
    config = load_dict(path_to_config)
    last_checkpoint, training_args, parameters, tokenizer, model, data_collator, train_dataset, eval_dataset, test_dataset, trial_complete, optimizers, callbacks = reinit_run(
        trial_checkpoint, 
        config, 
        AutoModelForMaskedLM,
        data_dir,
        group=group,
        preprocessed_data=preprocessed_data,
        pause_on_epoch=pause_on_epoch
        )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        optimizers=optimizers,
        callbacks=callbacks
    )

    print_run_init(model, config, parameters, trial_checkpoint, reinit=True)

    trainer.train(resume_from_checkpoint=last_checkpoint)

    complete = check_if_complete(trainer, parameters)
    
    if complete:
        complete_trial(trainer, test_dataset, parameters, trial_checkpoint, trial_complete)