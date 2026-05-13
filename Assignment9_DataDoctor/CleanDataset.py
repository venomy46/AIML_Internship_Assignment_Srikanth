import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

# Check missing values
print("Missing Values:\n", data.isnull().sum())

# Handle missing values (fill with mean for numeric columns)
data = data.fillna(data.mean(numeric_only=True))

# Remove duplicate rows
data = data.drop_duplicates()

# Standardize text (convert text columns to lowercase)
for column in data.select_dtypes(include='object'):
    data[column] = data[column].str.lower().str.strip()

# Display cleaned data
print("\nCleaned Dataset:")
print(data.head())