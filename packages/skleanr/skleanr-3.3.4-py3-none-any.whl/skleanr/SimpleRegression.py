# Simple Linear Regression without using SKLearn (Equation Given)

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + 2 + 0.1 * np.random.randn(100, 1)  # y = 3X + 2 + noise

# Calculate mean of X and y
x_mean = np.mean(X)
print("Mean of X : ", x_mean)
y_mean = np.mean(y)
print("Mean of Y : ", y_mean)

# Calculate slope (m) and intercept (b) using closed-form formulas
numerator = np.sum((X - x_mean) * (y - y_mean))
denominator = np.sum((X - x_mean) ** 2)
slope = numerator / denominator
intercept = y_mean - slope * x_mean

print("The slope and Intercept are:-")
print("Slope:", slope)
print("Intercept:", intercept)

plt.scatter(X, y, label='Data Points')
plt.plot(X, slope * X + intercept, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()




# Simple Linear Regression without using SKLearn(Data Given not equation)

import matplotlib.pyplot as plt
import numpy as np
import math


x = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
y = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

# plt.scatter(x, y)
# plt.show()

mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_x, "," , mean_y)

l=len(x)
numerator=0
denominator=0
for i in range(l):
  numerator += (x[i] - mean_x) * (y[i] - mean_y)
  denominator += (x[i] - mean_x) **2
m = numerator / denominator
c = mean_y - (m * mean_x)
print(m,c)


max_x = np.max(x) + 100
min_x = np.min(y) - 100
X = np.linspace(min_x,max_x,100)
Y = c + m*X

plt.plot(X, Y, color='green', label = 'Regression Line')
plt.scatter(x, y, c = 'black', label = 'data')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()