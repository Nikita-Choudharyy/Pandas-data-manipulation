# =========================================================
# Topic: DateTime Handling in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Name": ["Nikita", "Aman", "Priya", "Rahul", "Simran"],
    "Joining_Date": [
        "2024-01-15",
        "2023-08-20",
        "2024-03-10",
        "2022-12-05",
        "2024-06-01"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =========================================================
# Converting String to DateTime
# =========================================================

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nAfter DateTime Conversion:")
print(df)

# =========================================================
# Checking Data Types
# =========================================================

print("\nData Types:")
print(df.dtypes)

# =========================================================
# Extracting Year
# =========================================================

df["Year"] = df["Joining_Date"].dt.year

print("\nYear:")
print(df[["Name", "Year"]])

# =========================================================
# Extracting Month
# =========================================================

df["Month"] = df["Joining_Date"].dt.month

print("\nMonth:")
print(df[["Name", "Month"]])

# =========================================================
# Extracting Day
# =========================================================

df["Day"] = df["Joining_Date"].dt.day

print("\nDay:")
print(df[["Name", "Day"]])

# =========================================================
# Extracting Month Name
# =========================================================

df["Month_Name"] = df["Joining_Date"].dt.month_name()

print("\nMonth Name:")
print(df[["Name", "Month_Name"]])

# =========================================================
# Extracting Day Name
# =========================================================

df["Day_Name"] = df["Joining_Date"].dt.day_name()

print("\nDay Name:")
print(df[["Name", "Day_Name"]])

# =========================================================
# Finding the Earliest Date
# =========================================================

print("\nEarliest Joining Date:")
print(df["Joining_Date"].min())

# =========================================================
# Finding the Latest Date
# =========================================================

print("\nLatest Joining Date:")
print(df["Joining_Date"].max())

# =========================================================
# Calculating Days Since Joining
# =========================================================

today = pd.Timestamp.today()

df["Days_Since_Joining"] = (today - df["Joining_Date"]).dt.days

print("\nDays Since Joining:")
print(df[["Name", "Days_Since_Joining"]])

# =========================================================
# Sorting by Date
# =========================================================

print("\nSorted by Joining Date:")
print(df.sort_values(by="Joining_Date"))

# =========================================================
# Summary
# =========================================================

# - pd.to_datetime() converts strings into datetime format.
# - .dt.year extracts the year.
# - .dt.month extracts the month number.
# - .dt.day extracts the day.
# - .dt.month_name() returns month names.
# - .dt.day_name() returns weekday names.
# - min() and max() find date ranges.
# - Date subtraction helps calculate durations.
# - sort_values() can sort records by date.
