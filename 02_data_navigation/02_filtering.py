# =========================================================
# Topic: Filtering Data in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Name": ["Nikita", "Aman", "Priya", "Rahul", "Simran"],
    "Age": [22, 21, 23, 24, 20],
    "City": ["Jaipur", "Delhi", "Mumbai", "Pune", "Delhi"],
    "Salary": [50000, 45000, 60000, 55000, 40000]
}

df = pd.DataFrame(data)

print(df)

# =========================================================
# Filtering Rows Based on a Single Condition
# =========================================================

print("\nEmployees with Salary > 50000:")
print(df[df["Salary"] > 50000])

# =========================================================
# Filtering Rows Based on Age
# =========================================================

print("\nPeople Older Than 22:")
print(df[df["Age"] > 22])

# =========================================================
# Filtering Rows Based on String Values
# =========================================================

print("\nPeople From Delhi:")
print(df[df["City"] == "Delhi"])

# =========================================================
# Multiple Conditions Using &
# =========================================================

print("\nSalary > 45000 and Age > 22:")
print(df[(df["Salary"] > 45000) & (df["Age"] > 22)])

# =========================================================
# Multiple Conditions Using |
# =========================================================

print("\nCity is Delhi or Mumbai:")
print(df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")])

# =========================================================
# Using isin()
# =========================================================

print("\nPeople From Delhi or Pune:")
print(df[df["City"].isin(["Delhi", "Pune"])])

# =========================================================
# Summary
# =========================================================

# - Filtering helps select specific rows from a DataFrame.
# - Conditions return True or False values.
# - '&' is used for AND conditions.
# - '|' is used for OR conditions.
# - isin() checks multiple values at once.
