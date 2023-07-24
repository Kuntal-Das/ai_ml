import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# Standardize the features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Perform PCA with 2 principal components
n_components = 2
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_std)

# Create a DataFrame for the principal components
pca_df = pd.DataFrame(data=X_pca, columns=[f"PC{i + 1}" for i in range(n_components)])

# Add the target class to the DataFrame
pca_df["Target"] = y

# Visualize the results
plt.figure(figsize=(8, 6))
for target in np.unique(y):
    plt.scatter(
        pca_df.loc[pca_df["Target"] == target, "PC1"],
        pca_df.loc[pca_df["Target"] == target, "PC2"],
        label=iris.target_names[target],
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Principal Component Analysis on Iris Dataset")
plt.legend()
plt.grid(True)
plt.show()
