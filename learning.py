#Methods:enumerate(), capitalize(), title()
waiting_list = ["sen", "ben", "john"]
for index, i in enumerate(waiting_list):
    print(index + 1, i.capitalize())

names = ["sen jackson", "ben alderson", "john star"]
for index, i in enumerate(names):
    print(f"{index + 1}.{i.title()}")

#Methods: append(), replace(), pop()
todos = []
todo = input("Enter a todo: ")
todos.append(todo)

#Methods: replace(). Replace a symbol in a string: for-loop, list
filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentation.txt"]
for i in filenames:
    i = i.replace('.', ')', 1)
    print(i)

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

#Methods: sort() -DESC sorting (A-Z; 0-9)
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
#create a new list and add the title() method for each loop iteration
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