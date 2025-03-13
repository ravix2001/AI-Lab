import numpy as np
import matplotlib.pyplot as plt

# Inputs and Target Output
X = np.array([[1.5, 0.625]])  # Input features as a 2D array
y = np.array([0.5])  # Target output

# Random initialization of weights
W = np.random.randn(2)  # Two weights (for X1 and X2)
print("Initial Weights:", W)

# Hyperparameters
epochs = 20
alpha = 0.1

# To store error values during training
errorList = []

# Function to compute output of the perceptron (forward pass)
def forward_pass(X, W):
    return np.dot(X, W)  # Linear combination of inputs and weights

# Training Loop
for epoch in range(epochs):
    # Forward Pass
    y_out = forward_pass(X, W)

    # Compute the Error (Mean Squared Error)
    error = np.mean(np.square(y - y_out))
    errorList.append(error)

    # Compute Gradients
    gradient_W = -2 * np.dot((y - y_out), X)

    # Update Weights using Gradient Descent
    W = W - alpha * gradient_W

    # Print progress
    print(f"Epoch {epoch + 1}/{epochs}, Error: {error:.4f}")

# Final Weights
print("Final Weights:", W)

print(y_out)

# Plotting Error vs Epochs
plt.plot(range(epochs), errorList)
plt.xlabel("Epochs")
plt.ylabel("Error")
plt.title("Epochs vs Error")
plt.show()

# Test the model with the final weights
final_output = forward_pass(X, W)
print("Final Output:", final_output)
