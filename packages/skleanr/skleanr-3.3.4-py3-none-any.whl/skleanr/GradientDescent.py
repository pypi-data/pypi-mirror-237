import numpy as np
import math
import matplotlib.pyplot as plt

# Define the objective function you want to minimize.
def objective_function(x):
    # This is a simple quadratic function (a parabola).
    # f(x) = (x-2)^2 + (x-0)^2
    return (x - 2)**2 + (x - 0)**2

# Define the gradient of the objective function.
def gradient(x):
    # The gradient represents the slope of the function at a given point.
    # For this function, the gradient is 2 times the input 'x'.
    return 2 * x

# Set the learning rate, which determines the step size in each iteration.
learning_rate = 0.1

# Set an initial value for 'x', where the optimization process will start.
initial_x = 5

# Specify the number of iterations to perform during the gradient descent process.
num_iterations = 200

# Initialize 'x' with the initial value.
x = initial_x

# Create lists to keep track of the history of 'x' and the value of the objective function during optimization.
x_history = [x]
loss_history = [objective_function(x)]

# Perform gradient descent for a specified number of iterations.
for i in range(num_iterations):
    # Compute the gradient of the objective function at the current 'x'.
    grad = gradient(x)

    # Update 'x' by moving it in the direction of steepest descent (opposite to the gradient) with a step determined by the learning rate.
    x -= learning_rate * grad

    # Append the updated 'x' and the value of the objective function at the new 'x' to their respective histories.
    x_history.append(x)
    loss_history.append(objective_function(x))

# Create a range of 'x' values to plot the objective function.
x_values = np.linspace(-6, 6, 400)

# Compute the corresponding values of the objective function.
y_values = objective_function(x_values)

# Plot the objective function and the history of 'x' values during optimization.
plt.plot(x_values, y_values, label='Objective Function')
plt.scatter(x_history, loss_history, color='red', label='Gradient Descent Steps')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent Optimization')
plt.legend()

# Display the plot.
plt.show()
