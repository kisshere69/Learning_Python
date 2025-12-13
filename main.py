import csv
import json

#Read data from JSON
with open("users.json", "r") as file:
    users = json.load(file)

filtered_users = []

#Filter users aged 18 or older and add full_name
for user in users:
    if user["age"] >= 18:
        user["full_name"] = f"{user['first_name']} {user['last_name']}"
        filtered_users.append(user)

fieldnames = ["full_name", "age", "city"]

#Save the result as a CSV file
with open("filtered_users.csv", "w", newline = "") as file:

    #Create a CSV writer and ignore extra fields
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(filtered_users)

#Print the result
print("Done!")