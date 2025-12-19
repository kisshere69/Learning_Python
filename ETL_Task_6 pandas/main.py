import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv("employees.csv")

"""-----Check the structure-----"""
# Show first rows
print(df.head())

# Show structure and data types
print(df.info())

"""-----Transform DataFrame-----"""
# Replace empty names
df["name"] = df["name"].fillna("N/A")

# Remove rows with missing salary
df = df.dropna(subset=["salary"])

# Convert salary to numeric, invalid values -> NaN
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

print(df)

# Group by department
summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    employees = ("id", "count")
)

# Round average salary
summary["average_salary"] = summary["average_salary"].round(2)

print(summary)

# Save to CSV
summary.to_csv("summary_per_department.csv")

# Save to JSON
summary.to_json("summary_per_department.json", indent = 4)