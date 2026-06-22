# =========================================================
# Topic: Merge, Join and Concat in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating DataFrames
# =========================================================

employees = pd.DataFrame(
    {
        "Employee_ID": [101, 102, 103, 104],
        "Name": ["Nikita", "Aman", "Priya", "Rahul"],
        "Department_ID": [1, 2, 1, 3]
    }
)

departments = pd.DataFrame(
    {
        "Department_ID": [1, 2, 3],
        "Department_Name": ["IT", "HR", "Finance"]
    }
)

print("Employees DataFrame:")
print(employees)

print("\nDepartments DataFrame:")
print(departments)

# =========================================================
# Inner Merge
# =========================================================

inner_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="inner"
)

print("\nInner Merge:")
print(inner_merge)

# =========================================================
# Left Merge
# =========================================================

left_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="left"
)

print("\nLeft Merge:")
print(left_merge)

# =========================================================
# Right Merge
# =========================================================

right_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="right"
)

print("\nRight Merge:")
print(right_merge)

# =========================================================
# Outer Merge
# =========================================================

outer_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="outer"
)

print("\nOuter Merge:")
print(outer_merge)

# =========================================================
# Join Example
# =========================================================

employees_index = employees.set_index("Department_ID")
departments_index = departments.set_index("Department_ID")

joined_df = employees_index.join(
    departments_index,
    how="left"
)

print("\nJoin Example:")
print(joined_df)

# =========================================================
# Concat Example (Row-wise)
# =========================================================

df1 = pd.DataFrame(
    {
        "Name": ["Nikita", "Aman"],
        "Salary": [50000, 45000]
    }
)

df2 = pd.DataFrame(
    {
        "Name": ["Priya", "Rahul"],
        "Salary": [60000, 55000]
    }
)

concat_rows = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("\nRow-wise Concat:")
print(concat_rows)

# =========================================================
# Concat Example (Column-wise)
# =========================================================

city_df = pd.DataFrame(
    {
        "City": ["Jaipur", "Delhi", "Mumbai", "Pune"]
    }
)

concat_columns = pd.concat(
    [concat_rows, city_df],
    axis=1
)

print("\nColumn-wise Concat:")
print(concat_columns)

# =========================================================
# Summary
# =========================================================

# - merge() combines DataFrames using common columns.
# - inner keeps matching records only.
# - left keeps all records from the left DataFrame.
# - right keeps all records from the right DataFrame.
# - outer keeps all records from both DataFrames.
# - join() combines DataFrames using indexes.
# - concat() stacks DataFrames row-wise or column-wise.
