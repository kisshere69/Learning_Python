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

        # Initialize department if not exists. Department ("IT") = key; salary and count = values.
        if department not in departments:
            departments[department] = {
                "total_salary": 0,
                "count": 0
            }

        # Aggregate salary data
        departments[department]["total_salary"] += salary
        departments[department]["count"] += 1

# ----------------- LOAD -----------------

result = {}
final_result = []

#Obtain pairs of items from departments{}. Department = key; data = value.
for department, data in departments.items():
    avg_salary = round(data["total_salary"] / data["count"], 2)

#Write new fields in a new dictionary result{}
    result[department] = {
        "employees_count": data["count"],
        "average_salary": avg_salary
    }

#Calculate the average salary to write it in a CSV file
for department, stats in departments.items():
    average_salary = stats["total_salary"] / stats["count"]

    final_result.append({
    "department": department,
    "average_salary": round(average_salary, 2),
    "employees": stats["count"]
    })

# Save result to JSON
with open("clean_employees.json", "w", encoding="utf-8") as jsonfile:
    json.dump(result, jsonfile, indent=4)

print("ETL process completed successfully! Check the file.")


# Save result to CSV
with open("department_salary_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["department", "average_salary", "employees"]
    )

    writer.writeheader()
    writer.writerows(final_result)