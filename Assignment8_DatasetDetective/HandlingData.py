import pandas as pd

# Load dataset (example: CSV file)
data = pd.read_csv("data.csv")

# Display top rows
print("Top 5 Rows:")
print(data.head())

# Find highest value column (numeric)
highest_column = data.max(numeric_only=True)
print("\nHighest Values in Each Numeric Column:")
print(highest_column)

# Count missing values
missing_values = data.isnull().sum()
print("\nMissing Values Count:")
print(missing_values)