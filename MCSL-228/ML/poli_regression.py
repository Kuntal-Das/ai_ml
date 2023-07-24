import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Diabetes dataset
diabetes = load_diabetes()
X = diabetes.data  # Features
y = diabetes.target  # Target variable

def polynomial_regression(X, y, degree):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    return model

def plot_polynomial_fit(X, y, model):
    plt.scatter(X[:, 2], y, color='blue', label='Data points')
    
    # Sort the X values for smooth plotting of the polynomial fit
    X_sorted = np.sort(X[:, 2])
    X_poly_sorted = poly_features.fit_transform(X_sorted.reshape(-1, 1))
    y_pred = model.predict(X_poly_sorted)
    
    plt.plot(X_sorted[:, 0], y_pred, color='red', label='Polynomial Fit')
    plt.xlabel('BMI (Body Mass Index)')
    plt.ylabel('Diabetes Progression After One Year')
    plt.legend()
    plt.title('Polynomial Regression on Diabetes Dataset')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Set the degree of the polynomial regression
    degree = 3
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Perform polynomial regression on the training data
    model = polynomial_regression(X_train, y_train, degree)
    
    # Predict y for the test data
    X_test_poly = poly_features.transform(X_test[:, 2].reshape(-1, 1))
    y_pred = model.predict(X_test_poly)
    
    # Calculate the Mean Squared Error (MSE) as a measure of performance
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    
    # Plot the polynomial fit on the test data
    plot_polynomial_fit(X_test, y_test, model)
