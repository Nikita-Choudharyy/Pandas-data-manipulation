# =========================================================
# Topic: Data Selection in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Name": ["Nikita", "Aman", "Priya", "Rahul"],
    "Age": [22, 21, 23, 24],
    "City": ["Jaipur", "Delhi", "Mumbai", "Pune"],
    "Salary": [50000, 45000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)

# =========================================================
# Selecting a Single Column
# =========================================================

print("\nName Column:")
print(df["Name"])

# =========================================================
# Selecting Multiple Columns
# =========================================================

print("\nName and Salary Columns:")
print(df[["Name", "Salary"]])

# =========================================================
# Checking Data Type of Selection
# =========================================================

print("\nType of Single Column:")
print(type(df["Name"]))

print("\nType of Multiple Columns:")
print(type(df[["Name", "Salary"]]))

# =========================================================
# Selecting All Columns
# =========================================================

print("\nAll Columns:")
print(df.columns)

# =========================================================
# Summary
# =========================================================

# - Single column selection returns a Series.
# - Multiple column selection returns a DataFrame.
# - Columns are selected using square brackets [].
# - Data selection is the foundation of data analysis.
