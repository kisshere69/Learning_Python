#Methods: enumerate(), capitalize()
waiting_list = ["sen", "ben", "john"]
for index, i in enumerate(waiting_list):
    print(index + 1, i.capitalize())

#Methods: enumerate(), title()
names = ["sen jackson", "ben alderson", "john star"]
for index, i in enumerate(names):
    print(f"{index + 1}.{i.title()}")

#Methods: append()
todos = []
todo = input("Enter a todo: ")
todos.append(todo)

#Methods: replace(). Replace a symbol in a string.
filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentation.txt"]
for i in filenames:
    i = i.replace('.', ')', 1)
    print(i)

#Methods: replace() in a list comprehension
filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [filename.replace('.', '-') + ".txt" for filename in filenames]
print(filenames)

#Methods: delete a string by using pop()
todos = []
todo_number = int(input("Select a todo to complete: ")) - 1
todos.pop(todo_number)

#Methods: sort() -ASC sorting (A-Z; 0-9)
my_list = ["3", "2", "a", "4", "1", "c", "b", "d"]
my_list.sort()
print(my_list)

#Methods: sort() -DESC sorting (Z-A; 9-0)
my_list = ["3", "2", "a", "4", "1", "c", "b", "d"]
my_list.sort(reverse=True)
print(my_list)

#Methods and functions: open(), writelines(), readlines(). Read and write files
todos = []

todo = input("Enter a todo: ") + "\n"
todos.append(todo)

file = open('todos.txt', 'w')
file.writelines(todos)

todo = input("Enter a todo: ") + "\n"
file = open('todos.txt', 'r')
todos = file.readlines()

#Create a simple todo list: input, methods, match-case, while-loop, list, for-list, f-string, with as, read/write files
while True:
    #expect the user enter one of the actions
    user_action = input("Type add/show/replace/delete/exit: ").strip()

    #check the action. match if success, print out the error if wrong input
    match user_action:
        case "add":
            #expect the user enter a string
            todo = input("Enter a todo: ") + "\n"
            #open a file where this string will be stored and append the string to the end.
            with open("todos.txt", "a") as file:
                file.write(todo)

        case "show":
            #open a file
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            #print out the numbered items from the file
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")

        case "replace":
            #open a file
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            #expecet the user to enter the index value
            number = int(input("Select a todo to replace (1 - ...): ")) - 1

            #expect the user to enter a string for replacement
            new_todo = input("Enter new todo: ") + "\n"

            #save the new string in the same place (index)
            todos[number] = new_todo
            print("New Todo Has Been Saved!")

            #open a file and overwrite the string
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "delete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            #expect the integer for the index
            number = int(input("Select a todo to delete: ")) - 1
            #delete the index by the entered number. number value = index in a string
            todos.pop(number)

            #update the file
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break

        case _:
            print("Invalid input.")

#Define a tuple of color codes: tuples
color_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

#Numbered list: enumerate(), capitalize() and f-string
filenames = ['document', 'report', 'presentation']
for index, i in enumerate(filenames):
    print(f"{index}-{i.capitalize()}.txt")

#Check the length of a list, of a for-loop and of a string
todos = [1,2,3]
print("Length is:",len(todos))

a = enumerate("Hello World")
list(a)

mylist = ['a', 'b', 'c', 'd']
for i in mylist:
    print(len(mylist))

with open("todos.txt", "r") as file:
    file_content = file.readlines()

for i in file_content:
    print(f"The file contains {len(i)} characters.")

#Create .txt files and populate them with info
contents = ['All carrots are to be sliced'
            'longitudinally.',
            'The carrots were reportedly sliced.',
            'The sliced carrots are to be reported.']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    with open(f"files/{filename}", "w") as file:
        file.write(content)

#Create a program that prompts a user to enter new member name
new_member = input("Enter new member name: ") + "\n"
with open("members.txt", "a") as file:
    file.write(new_member)

#Create a program that reads the content of files and prints it out
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in zip(filenames):
    with open(f"{filename}", "r") as file:
        file = file.read()
        print(file)

#List comprehension. Faster when the code is easy (1 condition, 1 operation)
names = ["john smith", "jay santi", "eva kuki"]
capitalized = [name.title() for name in names]
print(capitalized)

#calculate the length of each string by using len() method
usernames = ["john 1990", "alberta1970", "magnola2000"]

length = [len(username) for username in usernames]
print(length)

#convert the strings to floats by using float() method
user_entries = ['10', '19.1', '20']

ue_floats = [float(ue) for ue in user_entries]
print(ue_floats)

#convert
numbers = [10, 20, 30]

num = [int(n * 2) for n in numbers]
print(num)

#calculate sum of the elements in a list
user_entries = ['10', '19.1', '20']

res = sum([float(i) for i in user_entries])
print(res)

#calculate the square using list comprehension
numbers = [1,2,4,6,10]
squared = [x*x for x in numbers]

print(squared)

#create a program that operates over each element in the list and
#creates the file with the element name + .txt and writes the content as an element name
languages = ['English', 'German', 'Spanish']

for i in languages:
    with open(f"{i}.txt", "w") as file:
        file.write(i)

#create a program that reads one file and copies its content into another
with open('story.txt', 'r') as file:
    content = file.read()

with open('story_copy.txt', 'w') as file:
    file.write(content)
    print(file.read())

#Calculate the % of a number, and display an error if invalid input
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")

#Print out the name of each file without an extension .txt
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for i in filenames:
    x = i[:-4]
    print(x)

#Print out an error if the input name is not in the waiting list. Check the name's index to see if a name exists.
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(name, "is not in the list of waiting list.")

#Create a function that prompts a user to enter a greeting
def greet():
    message = input("Enter a greeting: ").strip().title()
    return message

greeting = greet()
print(f"User's greeting: {greeting}")

#Create a function that calculates the average temperature and prints it out with 2 decimal places
try:
    def get_avg_temperature():
        with open('files_test/data.txt') as file:
            temperatures = [float(line) for line in file]
        return sum(temperatures) / len(temperatures)

    avg = get_avg_temperature()
    print(f'Average temperature: {avg:.2f}')

except ValueError:
    print(f"Invalid data in the file {__file__}\n!!!Please check the file and run the program again.")
    exit()

#create a function to calculate the average from the list
def avg_value(my_list):
    return sum(my_list) / len(my_list)

print(avg_value([10,20,30,40]))

#create a function to calculate the speed
def speed(distance, time):
    return distance / time

print(speed(200, 4))

#Create a function that returns the maximum value from a list
def get_max():
    grades = [9.6, 9.2, 9.7]

    max_value = max(grades)
    return max_value

print(get_max())

#Create a function that returns the maximum and minimum values from a list
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return maximum, minimum

print(f"Max: {get_max()[0]}, Min: {get_max()[1]}")

#Create a function that formats filenames
def format_filename():
    filename = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
    alt_filename = [fname.capitalize()[:-4] for fname in filename]
    return alt_filename

print(format_filename())

#Create a function that squares a number
def square_number():
    number = 5
    result = pow(number, 2)

    return result


print(square_number())

#Decoupling
feet_inches = input("Enter feet and inches(example: 4.2): ")

#decouple the input into two parts
def parse(feet_inches_local):
    parts = feet_inches_local.split(".")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

#convert the decoupled values to meters
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

#a cleaner version of the variable that stores the result of the parse function
f, i = parse(feet_inches)
print("intermediate result of a parse function:", f"feet is {f}, inches are {i}")

result = convert(f, i)

if result <= 1:
    print(f"{result:.2f} meters. The height is less than 1 meter. You can't go jumping :(")
else:
    print(f"{result:.2f} meters. You can go jumping!")

#create a function that decouples the string and prints out the number of words
user_str = "john, alex, sam"

def get_nr_items(user_input):
    words = user_input.split(",")
    return len(words)

res = get_nr_items(user_str)
print(res)


# Define a function named strength that takes one parameter, password
user_input = input("Enter a password: ").strip()

def strength(password):
    # Create an empty dictionary to store the strength attributes
    result = {}

    # Check the length of the password
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    # Check if the password contains a digit and an uppercase letter
    digit = False
    uppercase = False
    lowercase = False

    # Iterate over each character in the password
    for i in password:
        # Check if the character is a digit
        if i.isdigit():
            digit = True
        # Check if the character is an uppercase letter
        if i.isupper():
            uppercase = True
        # Check if the character is a lowercase letter
        if i.islower():
            lowercase = True

    # Store the results in the dictionary
    result["digits"] = digit
    result["upper-case"] = uppercase
    result["lower-case"] = lowercase

    print(result)

    # Check if all the strength attributes are True
    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"

print(strength(user_input))

#Docstrings
text = """
Hello.
My name is Nikita.
It's really nice to meet you!
I hope we will work together effectively
"""
print(text)

#Importing functions
"""
import the functions get_todos and write_todos from an external file
"""
"""
Or import functions. 
But then, you would need to write functions.get_todos() 
and functions.write_todos() 
"""

#Working within external files
"""
the below code is printed out only in "functions" file (external file)

the rest (defined functions) is being executed 
and printed out in the "app" file (internal file)
"""
if __name__ == "__main__":
    print("Hello from the functions!")

#importing functions from an external dir, file

#Display the time, date, day, month, year, time zone
import time
from datetime import datetime

date = time.strftime("%B %d, %Y")
print("Date:", date)
time = time.strftime("%H:%M:%S")
print("Time:", time)
now = datetime.now().astimezone()
print("Time zone(UTC):",now.tzinfo, now.utcoffset())

#Access the contents of all .txt, .py... files
import glob

myfiles = glob.glob("files/*.txt")
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

#Read the contents of the .csv file (files/sites.csv) and print it out
import csv

with open("read_csv/sites.csv") as csvfile:
    data =list(csv.reader(csvfile))

site = input("Site: ")
print("Below is the info about site", site)

site_info = data[0]
print(site_info)

for row in data:
    if row[0] == site:
        print(row[0:3])

#Create the .zip file and read its contents
import shutil

shutil.make_archive("output", "zip", "journal")

#Open the browser by the user's search input
import webbrowser

user_term = input("Enter the term: ")

webbrowser.open("https://google.com/search?q=" + user_term)

#Dictionary: Create a dictionary with students and their groups, and return it as Group: ['name']
students = {
    "Alice": "Group 1",
    "Bob": "Group 2",
    "Charlie": "Group 1",
    "Diana": "Group 3"
}

groups = {}
for name, grp in students.items():
    groups.setdefault(grp, []).append(name)

print(groups)

#Transform JSON text into Python objects. Load strings.
import json

with open("questions.json", "r") as json_file:
    content = json_file.read()

data = json.loads(content)