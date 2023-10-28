import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        # Initialize the logistic regression model with learning rate and number of iterations
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        # Define the sigmoid function used for logistic regression
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # Train the logistic regression model with input data X and labels y
        num_samples, num_features = X.shape

        # Initialize weights and bias
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Iteratively update model parameters
        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear_model)

            # Calculate gradients for weights and bias
            dw = (1 / num_samples) * np.dot(X.T, (predictions - y))
            db = (1 / num_samples) * np.sum(predictions - y)

            # Update model parameters using gradients and learning rate
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, T):
        # Make predictions on new data T
        linear_model = np.dot(T, self.weights) + self.bias
        predictions = self.sigmoid(linear_model)

        # Convert predicted probabilities to binary labels (0 or 1)
        predicted_labels = [1 if p >= 0.5 else 0 for p in predictions]

        return predicted_labels

# Sample data
X = np.array([[2.5, 1.5], [3.0, 1.0], [4.0, 3.0], [1.0, 4.0], [2.0, 2.0]])
print("X: ", X)
Y = np.array([1, 1, 0, 0, 1])
print("Y: ", Y)

T = np.array([[2, 1], [3.0, 1.5], [4.0, 3.0], [1.0, 4.0], [2.5, 2.0]])

# Create a logistic regression model with specified parameters
model = LogisticRegression()

# Train the model on the sample data
model.fit(X, Y)

# Make predictions on new data
y_pred = model.predict(T)

# Print the learned weights and bias, as well as the predicted labels
print("Learned Weights:", model.weights)
print("Learned Bias:", model.bias)
print("Predicted Labels:", y_pred)
