# import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# define the data points for blue and red categories
blue = np.array([[1, 2], [2, 1], [1, -2], [2, -2]])
red = np.array([[4, -1], [4, 1], [5, -1], [6, 1]])

# combine both the categories
X = np.concatenate((blue, red))
# create label for blue and red categories
y = np.concatenate((np.ones(blue.shape[0]), -np.ones(red.shape[0])))

# fit the SVM model
model = svm.SVC(kernel='linear', C=1E10)
model.fit(X, y)

# get the support vectors and optimal separating line
support_vectors = model.support_vectors_
w = model.coef_
b = model.intercept_

# plot x=0 and y=0 lines
plt.axhline(y=0, color='gray')
plt.axvline(x=0, color='gray')

# set axis limits
plt.xlim([-10, 10])
plt.ylim([-10, 10])

# plot the data points and separating line
plt.scatter(blue[:, 0], blue[:, 1], color='blue', label='Blue')
plt.scatter(red[:, 0], red[:, 1], color='red', label='Red')
plt.scatter(support_vectors[:, 0], support_vectors[:, 1],
            color='none', label='Support Vectors', edgecolors='black')
# plt.plot([0, 7], [(-w[0]*0 - b)/w[1], (-w[0]*7 - b)/w[1]], color='black', label='Optimal Separating Line')
plt.plot(model.predict([[i, i] for i in range(-10, 10)]),
         color='green', label='Optimal Separating Line')
plt.legend()
plt.show()
