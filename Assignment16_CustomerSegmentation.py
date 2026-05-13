import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset (Annual Income vs Spending Score)
data = {
    "Income": [15, 16, 17, 18, 50, 55, 60, 62, 80, 85],
    "Spending": [39, 40, 42, 45, 60, 65, 70, 72, 20, 25]
}

df = pd.DataFrame(data)

# Apply K-Means
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

# Plot clusters
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()