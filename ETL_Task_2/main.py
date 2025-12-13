import requests
import pandas as pd
import sqlite3

# Load data from API
url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
todos = response.json()

# Filter completed tasks
completed_tasks = [task for task in todos if task["completed"]]

# Save to CSV
df = pd.DataFrame(completed_tasks)
df.to_csv("completed_tasks.csv", index=False)
print("Saved to completed_tasks.csv")

# Load CSV into pandas
df_loaded = pd.read_csv("completed_tasks.csv")

# Basic statistics
print("Total completed tasks:", len(df))
print(df_loaded.groupby("userId")["id"].count())

# Save to SQLite
conn = sqlite3.connect("completed_tasks.db")
df_loaded.to_sql("completed_tasks", conn, if_exists="replace", index=False)
print("Saved to completed_tasks.db")
conn.close()