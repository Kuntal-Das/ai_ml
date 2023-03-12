from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class KNN:
    def __init__(self, k=3):
        self.k = k

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1-x2)**2))

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        # compute the distances
        distances = [self.euclidean_distance(x, x_train) for x_train in self.X_train]

        # get the closest k
        k_indeces = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indeces]

        # get lable with majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]


if __name__ == '__main__':
    iris = load_iris()
    X, y = iris.data, iris.target  # type: ignore

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234)

    cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'], None)
    plt.figure()
    plt.scatter(X[:, 2], X[:, 3], c=y,
                cmap=cmap, edgecolor='k', s=20)
    plt.show()

    clf = KNN(k=3)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    acc = np.sum(preds == y_test)/len(y_test)
    print(f"Accuracy {acc*100}%")
