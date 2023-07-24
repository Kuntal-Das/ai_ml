import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

class KMeans:
    def __init__(self, k=3, epochs=100, min_variance=0.2):
        self.ks = k
        self.min_variance = min_variance
        self.wcss = 0
        self.epochs = epochs
        self.centroids = []
        self.cluster_grp = []

    def get_elbow(self, X):
        k = 1
        for k in range(1, self.ks):
            self._fit(X, k)
            new_wcss = self.get_wcss(X)
            pov = float('inf')
            if k > 1:
                pov = (self.wcss - new_wcss) / self.wcss
            print(f"no of clusters : {k} \t percentage of variance {pov}")
            self.plot(X)
            self.wcss = new_wcss
            if pov < self.min_variance:
                break
        return k

    def _fit(self, X, k):
        rand_indx = random.sample(range(0, X.shape[0]), k)
        self.centroids = X[rand_indx]
        for i in range(self.epochs):
            # assign clusters
            self.cluster_grp = self.assign_clusters(X)
            # move centroids
            new_centroids = self.move_centroids(X)
            # check function
            if (self.centroids == new_centroids).all():
                break
            self.centroids = new_centroids

        return self.cluster_grp

    # Assign cluster clusters based on closest centroid
    def assign_clusters(self, X):
        clusters_group = []
        for i in range(X.shape[0]):
            distances = self.euclidean_distance(self.centroids, X[i])
            cluster_no = [v for v, dist in enumerate(
                distances) if dist == min(distances)]
            clusters_group.append(cluster_no[0])
        return np.array(clusters_group)

    # Calculate new centroids based on each cluster's mean
    def move_centroids(self, X):
        new_centroids = []
        unique_clusters = np.unique(self.cluster_grp)
        for cluster_type in unique_clusters:
            new_centroids.append(
                X[self.cluster_grp == cluster_type].mean(axis=0))
        return np.array(new_centroids)

    def euclidean_distance(self, X1, X2):
        return np.sqrt(np.sum((X1 - X2)**2, axis=1))

    def get_wcss(self, X):
        new_wcss = 0
        for centroid_indx in range(len(self.centroids)):
            new_wcss += sum(self.euclidean_distance(
                X[self.cluster_grp == centroid_indx], self.centroids[centroid_indx]))
        return new_wcss

    def plot(self, X):
        plt.figure()
        for i in range(self.ks):
            plt.scatter(X[self.cluster_grp == i, 0],
                        X[self.cluster_grp == i, 1])
            plt.scatter(self.centroids[:, 0],
                        self.centroids[:, 1], color='black')
        plt.show()


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data

    km = KMeans(10, 1000)
    km.get_elbow(X)

    print("end")
