import wandb

# Initialize a new wandb run
wandb.init(project="my_project_name", entity="your_username_or_team")

# Log hyperparameters (optional)
wandb.config.learning_rate = 0.001
wandb.config.batch_size = 32

# Example of logging metrics
for epoch in range(10):
    # Assuming you have metrics like loss and accuracy
    loss = 0.1 * (epoch + 1)  # Dummy loss
    accuracy = 0.9 - (0.01 * epoch)  # Dummy accuracy
    
    # Log these metrics to Wandb
    wandb.log({"epoch": epoch, "loss": loss, "accuracy": accuracy})
