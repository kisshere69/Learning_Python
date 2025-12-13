import csv
import json

clean_data = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    """
    csv.DictReader reads CSV files as dictionaries
    keys are taken from the first line (id, name,...)
    """
    #Transform data: remove spaces and convert names to Title Case
    for row in reader:
        name = row["name"].strip().title()
        department = row["department"].strip()
        email = row["email"].strip()
        salary = row["salary"].strip()

        """Checks"""

        #Check 1: Skip rows if they don't contain the following fields
        if not id or not salary or not email:
            continue #Skip empty fields

        #Check 2: Skip rows if salary is not a valid number
        try:
            salary_int = int(salary)
        except (ValueError, TypeError):
            continue

        if salary_int < 4000:
            continue

        #Check 3: Skip rows if email is not valid
        if "@" not in email:
            continue #Skip invalid email

        """Form a clean structure"""

        clean_data.append({
            "id": int(row["id"].strip()),
            "name": name,
            "department": department,
            "salary": int(salary),
            "email": email
        })

        #Save the clean data to a JSON file
        with open("clean_employees.json", "w") as json_file:
            json.dump(clean_data, json_file, indent=4)