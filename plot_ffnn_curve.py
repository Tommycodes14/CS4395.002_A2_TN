import matplotlib.pyplot as plt

# Example data from your FFNN training
epochs = [1, 2, 3]
training_loss = [1.1, 0.95, 0.82]  # <-- You can estimate these from your training logs
validation_accuracy = [54.88, 59.25, 57.63]  # From your real results

fig, ax1 = plt.subplots()

# Plot training loss on left y-axis
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Training Loss', color='tab:blue')
ax1.plot(epochs, training_loss, label='Training Loss', color='tab:blue', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for validation accuracy
ax2 = ax1.twinx()
ax2.set_ylabel('Validation Accuracy (%)', color='tab:green')
ax2.plot(epochs, validation_accuracy, label='Validation Accuracy', color='tab:green', marker='x')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Title and layout
plt.title('FFNN Learning Curve')
fig.tight_layout()
plt.grid(True)
plt.show()
