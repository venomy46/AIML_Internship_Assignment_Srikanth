import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset (example: Mall Customers dataset)
data = pd.read_csv("Mall_Customers.csv")

# Select relevant features
X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5)
data["Cluster"] = kmeans.fit_predict(X)

# Plot clusters
plt.scatter(X["Annual Income (k$)"], X["Spending Score (1-100)"], c=data["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()