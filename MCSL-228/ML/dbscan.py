import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

# Generating a sample dataset of 2D points
def create_dataset():
    X, y = make_blobs(n_samples=500, centers=3, random_state=42, cluster_std=1.0)
    return X

# Implement DBSCAN Algorithm
def dbscan_algorithm(X, eps, min_samples):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X)
    return labels

# Main function to run the DBSCAN algorithm and visualize the clusters
def main():
    # Create the dataset
    dataset = create_dataset()

    # DBSCAN hyperparameters
    eps = 0.5  # Maximum distance between two samples to be considered as in the same neighborhood
    min_samples = 5  # Minimum number of samples required in a neighborhood to be considered as a core point

    # Run DBSCAN algorithm
    labels = dbscan_algorithm(dataset, eps, min_samples)

    # Visualize the clusters
    unique_labels = np.unique(labels)
    num_clusters = len(unique_labels) - 1  # Excluding the noise points (cluster label -1)

    plt.figure(figsize=(8, 6))
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = 'k'  # Black color for noise points (cluster label -1)

        class_member_mask = (labels == k)
        xy = dataset[class_member_mask]
        plt.scatter(xy[:, 0], xy[:, 1], c=col, label=f'Cluster {k}')

    plt.title(f'DBSCAN Clustering with {num_clusters} clusters')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
