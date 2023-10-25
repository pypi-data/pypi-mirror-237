from torch.utils.tensorboard import SummaryWriter
import torchvision

# Init writer and model
writer = SummaryWriter('runs/demo')
model = torchvision.models.resnet50()
dummy_data, _ = load_dataset()

# Add model graph
writer.add_graph(model, dummy_data)

# Fake training loop for demo
for epoch in range(5):
    loss = epoch * 0.1  # Simulated loss
    writer.add_scalar('train_loss', loss, epoch)

# Close writer
writer.close()