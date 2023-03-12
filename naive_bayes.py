# Import packages
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Import data
training = pd.read_csv('datasets/iris_train.csv')
test = pd.read_csv('datasets/iris_test.csv')


# Create the X, Y, Training and Test
xtrain = training.drop('Species', axis=1)
ytrain = training.loc[:, 'Species']
xtest = test.drop('Species', axis=1)
ytest = test.loc[:, 'Species']


# Init the Gaussian Classifier
model = GaussianNB()

# Train the model 
model.fit(xtrain, ytrain)

# Predict Output 
pred = model.predict(xtest)

# Plot Confusion Matrix
mat = confusion_matrix(pred, ytest)
names = np.unique(pred)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')

# # load the iris dataset
# from sklearn import metrics
# from sklearn.naive_bayes import GaussianNB
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris

# iris = load_iris()

# # store the feature matrix (X) and response vector (y)
# X = iris.data
# y = iris.target

# # splitting X and y into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.4, random_state=1)

# # training the model on training set
# gnb = GaussianNB()
# gnb.fit(X_train, y_train)

# # making predictions on the testing set
# y_pred = gnb.predict(X_test)

# # comparing actual response values (y_test) with predicted response values (y_pred)
# print("Gaussian Naive Bayes model accuracy(in %):",
#       metrics.accuracy_score(y_test, y_pred)*100)

# print(X_test, y_pred)
