# =========================================================
# Topic: String Operations in Pandas
# =========================================================

import pandas as pd

# =========================================================
# Creating a DataFrame
# =========================================================

data = {
    "Name": ["  Nikita  ", "AMAN", "Priya", "rahul", "Simran"],
    "Email": [
        "nikita@gmail.com",
        "aman@yahoo.com",
        "priya@gmail.com",
        "rahul@outlook.com",
        "simran@gmail.com"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =========================================================
# Convert to Lowercase
# =========================================================

df["Name_Lower"] = df["Name"].str.lower()

print("\nLowercase Names:")
print(df["Name_Lower"])

# =========================================================
# Convert to Uppercase
# =========================================================

df["Name_Upper"] = df["Name"].str.upper()

print("\nUppercase Names:")
print(df["Name_Upper"])

# =========================================================
# Remove Extra Spaces
# =========================================================

df["Name_Clean"] = df["Name"].str.strip()

print("\nNames After Removing Spaces:")
print(df["Name_Clean"])

# =========================================================
# Calculate String Length
# =========================================================

df["Name_Length"] = df["Name_Clean"].str.len()

print("\nName Length:")
print(df["Name_Length"])

# =========================================================
# Check if String Contains a Value
# =========================================================

print("\nGmail Users:")
print(df[df["Email"].str.contains("gmail")])

# =========================================================
# Replace Text
# =========================================================

df["Email"] = df["Email"].str.replace("gmail.com", "company.com")

print("\nEmails After Replacement:")
print(df["Email"])

# =========================================================
# Split Strings
# =========================================================

df["Username"] = df["Email"].str.split("@").str[0]

print("\nExtracted Usernames:")
print(df["Username"])

# =========================================================
# Summary
# =========================================================

# - str.lower() converts text to lowercase.
# - str.upper() converts text to uppercase.
# - str.strip() removes extra spaces.
# - str.len() calculates string length.
# - str.contains() searches text.
# - str.replace() replaces text.
# - str.split() splits strings into parts.
