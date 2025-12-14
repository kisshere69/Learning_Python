import csv
import json

# ----------------- EXTRACT -----------------


# Dictionary to store aggregated salary data
departments = {}

with open("employees.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        department = row["department"]
        salary_raw = row["salary"]

        # ----------------- TRANSFORM -----------------


        # Skip empty or invalid salary values
        try:
            salary = int(salary_raw)
        except (ValueError, TypeError):
            continue

        # Initialize department if not exists
        if department not in departments:
            departments[department] = {
                "total_salary": 0,
                "count": 0
            }

        # Aggregate salary data
        departments[department]["total_salary"] += salary
        departments[department]["count"] += 1

# ----------------- LOAD -----------------


# Prepare final result
result = {}

for department, data in departments.items():
    avg_salary = round(data["total_salary"] / data["count"], 2)

    result[department] = {
        "employees": data["count"],
        "average_salary": avg_salary
    }

# Save result to JSON
with open("clean_employees.json", "w", encoding="utf-8") as jsonfile:
    json.dump(result, jsonfile, indent=4)

print("ETL process completed successfully! Check the file.")