# =========================================================
# Topic: Pandas DataFrame Basics
# =========================================================

# A DataFrame is a two-dimensional labeled data structure
# consisting of rows and columns.

# Importing Pandas
import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Name": ["Nikita", "Aman", "Priya"],
    "Age": [22, 21, 23],
    "City": ["Jaipur", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)

# =========================================================
# Displaying Specific Columns
# =========================================================

print(df["Name"])

print(df["Age"])

# =========================================================
# DataFrame Attributes
# =========================================================

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData Types:")
print(df.dtypes)

print("\nSize:")
print(df.size)

# =========================================================
# Basic Information
# =========================================================

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nSummary Information:")
print(df.info())

# =========================================================
# Statistical Summary
# =========================================================

print(df.describe())

# =========================================================
# Summary
# =========================================================

# - DataFrame is a two-dimensional data structure.
# - Stores data in rows and columns.
# - Can contain multiple data types.
# - Provides attributes for understanding data.
# - Used extensively in data analysis and machine learning.
