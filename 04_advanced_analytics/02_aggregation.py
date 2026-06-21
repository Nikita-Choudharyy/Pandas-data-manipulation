# =========================================================
# Topic: Aggregation Functions in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "Employee": ["Nikita", "Aman", "Priya", "Rahul", "Simran", "Rohit", "Anjali"],
    "Salary": [60000, 45000, 70000, 55000, 50000, 65000, 80000],
    "Experience": [2, 1, 4, 3, 2, 5, 6]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =========================================================
# Basic Aggregations
# =========================================================

print("\nMean Salary:")
print(df["Salary"].mean())

print("\nMaximum Salary:")
print(df["Salary"].max())

print("\nMinimum Salary:")
print(df["Salary"].min())

print("\nTotal Salary:")
print(df["Salary"].sum())

print("\nMedian Salary:")
print(df["Salary"].median())

# =========================================================
# Multiple Aggregations on Salary
# =========================================================

print("\nSalary Aggregations:")
print(
    df["Salary"].agg(
        ["count", "min", "max", "mean", "median", "sum", "std"]
    )
)

# =========================================================
# Aggregations Using GroupBy
# =========================================================

print("\nDepartment-wise Salary Statistics:")
print(
    df.groupby("Department")["Salary"].agg(
        ["count", "min", "max", "mean", "sum"]
    )
)

# =========================================================
# Multiple Column Aggregation
# =========================================================

print("\nSalary and Experience Aggregation:")

print(
    df.groupby("Department").agg(
        {
            "Salary": ["min", "max", "mean"],
            "Experience": ["min", "max", "mean"]
        }
    )
)

# =========================================================
# Named Aggregation
# =========================================================

print("\nNamed Aggregation:")

result = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Highest_Salary=("Salary", "max"),
    Average_Experience=("Experience", "mean")
)

print(result)

# =========================================================
# Summary
# =========================================================

# - Aggregation summarizes data.
# - mean(), median(), sum(), min(), max() are common aggregations.
# - agg() applies multiple functions together.
# - Aggregation can be performed on single or multiple columns.
# - Named aggregation creates clean and readable output.
