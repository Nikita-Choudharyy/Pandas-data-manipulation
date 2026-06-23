# =========================================================
# Topic: Pivot Tables in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Gender": ["F", "M", "F", "M", "F", "M"],
    "Salary": [60000, 70000, 45000, 50000, 65000, 55000],
    "Experience": [2, 4, 1, 3, 5, 2]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =========================================================
# Basic Pivot Table
# =========================================================

pivot_salary = pd.pivot_table(
    df,
    values="Salary",
    index="Department"
)

print("\nAverage Salary by Department:")
print(pivot_salary)

# =========================================================
# Pivot Table with Multiple Columns
# =========================================================

pivot_gender = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender"
)

print("\nSalary by Department and Gender:")
print(pivot_gender)

# =========================================================
# Using Different Aggregation Functions
# =========================================================

pivot_sum = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="sum"
)

print("\nTotal Salary by Department:")
print(pivot_sum)

# =========================================================
# Multiple Aggregations
# =========================================================

pivot_multiple = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc=["mean", "min", "max"]
)

print("\nMultiple Aggregations:")
print(pivot_multiple)

# =========================================================
# Multiple Values
# =========================================================

pivot_multi_values = pd.pivot_table(
    df,
    values=["Salary", "Experience"],
    index="Department",
    aggfunc="mean"
)

print("\nAverage Salary and Experience:")
print(pivot_multi_values)

# =========================================================
# Pivot Table with Margins
# =========================================================

pivot_margins = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean",
    margins=True
)

print("\nPivot Table with Grand Total:")
print(pivot_margins)

# =========================================================
# Summary
# =========================================================

# - pivot_table() summarizes data efficiently.
# - index defines row grouping.
# - columns creates column categories.
# - values specifies the column to aggregate.
# - aggfunc controls the aggregation method.
# - margins=True adds grand totals.
# - Useful for reporting and exploratory data analysis.
