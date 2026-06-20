# =========================================================
# Topic: GroupBy Basics in Pandas
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
# Grouping by Department
# =========================================================

grouped = df.groupby("Department")

print("\nGroupBy Object:")
print(grouped)

# =========================================================
# Count Employees in Each Department
# =========================================================

print("\nEmployee Count:")
print(grouped["Employee"].count())

# =========================================================
# Average Salary by Department
# =========================================================

print("\nAverage Salary:")
print(grouped["Salary"].mean())

# =========================================================
# Maximum Salary by Department
# =========================================================

print("\nMaximum Salary:")
print(grouped["Salary"].max())

# =========================================================
# Minimum Salary by Department
# =========================================================

print("\nMinimum Salary:")
print(grouped["Salary"].min())

# =========================================================
# Total Salary by Department
# =========================================================

print("\nTotal Salary:")
print(grouped["Salary"].sum())

# =========================================================
# Average Experience by Department
# =========================================================

print("\nAverage Experience:")
print(grouped["Experience"].mean())

# =========================================================
# Multiple Aggregations
# =========================================================

print("\nMultiple Aggregations:")
print(
    grouped["Salary"].agg(
        ["count", "min", "max", "mean", "sum"]
    )
)

# =========================================================
# Grouping by Multiple Columns
# =========================================================

data2 = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Gender": ["F", "M", "F", "M", "F", "M"],
    "Salary": [60000, 70000, 45000, 50000, 65000, 55000]
}

df2 = pd.DataFrame(data2)

print("\nGroup By Department and Gender:")
print(
    df2.groupby(["Department", "Gender"])["Salary"].mean()
)

# =========================================================
# Summary
# =========================================================

# - groupby() splits data into groups.
# - count() counts records in each group.
# - mean() calculates average values.
# - min() and max() find extremes.
# - sum() calculates totals.
# - agg() performs multiple aggregations together.
# - groupby() can work with one or multiple columns.
