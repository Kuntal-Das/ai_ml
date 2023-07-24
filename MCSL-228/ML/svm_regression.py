import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import time

# Generate a random dataset for demonstration purposes
np.random.seed(time.thread_time_ns())
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(1/X).ravel()
y += 0.5 * np.random.randn(80)

# Create and fit the SVR model
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr_rbf.fit(X, y)

# Generate data for the plot
X_plot = np.linspace(0, 5, 100)[:, None]
y_pred = svr_rbf.predict(X_plot)

# Plot the results
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X_plot, y_pred, color='navy', label='RBF model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
