# =========================================================
# Topic: Pandas Series Basics
# =========================================================

# A Series is a one-dimensional labeled array in Pandas
# that can store data of any type.

# Importing Pandas
import pandas as pd

# =========================================================
# Creating a Series
# =========================================================

data = [10, 20, 30, 40, 50]

basic_series = pd.Series(data)

print(basic_series)

# =========================================================
# Accessing Elements
# =========================================================

print(basic_series[0])
print(basic_series[2])

# =========================================================
# Custom Index
# =========================================================

marks = pd.Series(
    [85, 90, 78],
    index=["Math", "Science", "English"]
)

print(marks)

print(marks["Math"])

# =========================================================
# Series Attributes
# =========================================================

print("Values:")
print(marks.values)

print("\nIndex:")
print(marks.index)

print("\nShape:")
print(marks.shape)

print("\nSize:")
print(marks.size)

print("\nData Type:")
print(marks.dtype)

# =========================================================
# Basic Operations
# =========================================================

numbers = pd.Series([1, 2, 3, 4, 5])

print(numbers + 10)
print(numbers * 2)

# =========================================================
# Summary
# =========================================================

# - Series is a one-dimensional data structure.
# - It stores labeled data.
# - Supports custom indexing.
# - Allows mathematical operations.
# - Forms the foundation of Pandas DataFrames.
