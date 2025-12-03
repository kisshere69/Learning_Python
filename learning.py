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
    user_action = input("Type add/show/replace/delete/exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open("todos.txt", "a") as file:
                file.write(todo)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}", end="")

        case "replace":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Select a todo to replace (1 - ...): ")) - 1
            new_todo = input("Enter new todo: ") + "\n"

            todos[number] = new_todo
            print("New Todo Has Been Saved!")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "delete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Select a todo to delete: ")) - 1
            todos.pop(number)

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