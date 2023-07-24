import numpy as np
import matplotlib.pyplot as plt

# Sample dataset (x and y values)
x = np.array([-2, -1, 0, 1, 2, 3, 4, 5])
y = np.array([15, 4, 1, 2, 5, 14, 27, 40])

def polynomial_regression(x, y, degree):
    coefficients = np.polyfit(x, y, degree)
    return coefficients

def predict(x, coefficients):
    return np.polyval(coefficients, x)

def plot_polynomial_fit(x, y, coefficients):
    plt.scatter(x, y, color='blue', label='Data points')
    plt.plot(x, predict(x, coefficients), color='red', label='Polynomial Fit')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.title('Polynomial Regression')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Set the degree of the polynomial regression
    degree = 3
    
    # Perform polynomial regression
    coefficients = polynomial_regression(x, y, degree)
    
    # Print the equation of the polynomial fit
    equation = ' + '.join([f"{coeff:.2f} * x^{i}" for i, coeff in enumerate(reversed(coefficients))])
    print(f"Polynomial fit equation: y = {equation}")
    
    # Predict y for a given x (e.g., x = 6)
    x_to_predict = 6
    predicted_y = predict(x_to_predict, coefficients)
    print(f"Predicted y for x = {x_to_predict}: {predicted_y:.2f}")
    
    # Plot the polynomial fit
    plot_polynomial_fit(x, y, coefficients)
