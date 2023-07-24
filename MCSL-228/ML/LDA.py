import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names

# # Convert the dataset into a pandas DataFrame
# columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# df = pd.DataFrame(data, columns=columns)
# df['target'] = target_names[target]

# Standardize the features for LDA
scaler = StandardScaler()
X_std = scaler.fit_transform(data)

# Perform Linear Discriminant Analysis
lda = LDA(n_components=2)
X_lda = lda.fit_transform(X_std, target)

# Create a new DataFrame with LDA components
lda_df = pd.DataFrame(data=X_lda, columns=['LD1', 'LD2'])
lda_df['target'] = target_names[target]

# Plot the LDA components
sns.scatterplot(x='LD1', y='LD2', hue='target', data=lda_df)
plt.title('Linear Discriminant Analysis (LDA)')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend()
plt.show()
