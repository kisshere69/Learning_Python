import csv
import json

# Load and read the CSV file
with open("employees.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

clean_data = []

# Clean and transform data
for row in rows:

    #Skip empty rows
    if not row["name"]:
        continue

    #Convert age to int
    age = row["age"].strip()
    age = int(age) if age.isdigit() else None

    #Fix salary
    salary = row["salary"].strip()
    if salary == "" or salary == "not available":
        salary = None
    else:
        salary = int(salary)

    name = row["name"].strip()
    if name == "" or name == "not available":
        name = None
    else:
        name = row["name"].strip()

    #Build clean record
    clean_row = {
        "name": name,
        "age": age,
        "salary": salary,
        "department": row["department"].strip(),
    }

    #Append the clean data to an empty list
    clean_data.append(clean_row)

#Filter employees over 30 years old. Create a list comprehension.
filtered = [emp for emp in clean_data if emp["age"] and emp["age"] > 20]

#Save the results into JSON. Create a file if it doesn't exist.
with open("employees_clean.json", 'w') as json_file:
    json.dump(filtered, json_file)

print("ETL Completed! Saved to employees_clean.json")