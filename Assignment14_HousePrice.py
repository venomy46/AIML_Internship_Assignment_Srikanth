from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset (House size in sq ft vs Price)
X = np.array([[500], [800], [1000], [1200], [1500]])
y = np.array([100000, 150000, 200000, 230000, 300000])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict price for new house size
new_size = np.array([[1100]])
predicted_price = model.predict(new_size)

print("Predicted House Price:", predicted_price[0])