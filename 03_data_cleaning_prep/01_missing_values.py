# =========================================================
# Topic: Handling Missing Values in Pandas
# =========================================================

import pandas as pd
import numpy as np

# =========================================================
# Creating a DataFrame with Missing Values
# =========================================================

data = {
    "Name": ["Nikita", "Aman", "Priya", None, "Simran"],
    "Age": [22, np.nan, 23, 24, np.nan],
    "City": ["Jaipur", "Delhi", None, "Pune", "Mumbai"],
    "Salary": [50000, 45000, np.nan, 55000, 40000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =========================================================
# Checking Missing Values
# =========================================================

print("\nMissing Values:")
print(df.isnull())

# =========================================================
# Counting Missing Values
# =========================================================

print("\nMissing Values Count:")
print(df.isnull().sum())

# =========================================================
# Checking if Any Missing Value Exists
# =========================================================

print("\nAny Missing Value Present?")
print(df.isnull().any())

# =========================================================
# Dropping Rows with Missing Values
# =========================================================

print("\nRows After dropna():")
print(df.dropna())

# =========================================================
# Filling Missing Values with a Constant
# =========================================================

filled_df = df.fillna("Unknown")

print("\nMissing Values Filled with 'Unknown':")
print(filled_df)

# =========================================================
# Filling Numerical Missing Values
# =========================================================

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAge Column Filled with Mean:")
print(df)

# =========================================================
# Summary
# =========================================================

# - isnull() identifies missing values.
# - sum() counts missing values.
# - dropna() removes missing data.
# - fillna() replaces missing values.
# - Mean, median, or custom values can be used for filling.
