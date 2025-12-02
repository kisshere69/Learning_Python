#Methods: enumerate(), capitalize(), title()
waiting_list = ["sen", "ben", "john"]
for index, i in enumerate(waiting_list):
    print(index + 1, i.capitalize())

names = ["sen jackson", "ben alderson", "john star"]
for name in names:
    print(name.title())

#Methods: append(), replace(), pop()
todos = []
todo = input("Enter a todo: ")
todos.append(todo)

#Replace a symbol in a string: for-loop, list
filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentation.txt"]
for i in filenames:
    i = i.replace('.', ')', 1)
    print(i)

#Methods: delete a string by using pop()
todos = []
todo_number = int(input("Select a todo to complete: ")) - 1
todos.pop(todo_number)

#Create a simple todo list: input, methods, match-case, while-loop, list, for-list, f-string
todos = []

while True:
    user_action = input("Type add/show/replace/complete/exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            print("Saved")
            todos.append(todo)
        case "show":
            for index, i in enumerate(todos):
                print(f"{index + 1}.{i}")
        case "replace":
            todo_number = int(input("Select a todo to replace(1 - ...): ")) - 1
            new_todo = input("Enter a new todo: ")
            todos[todo_number] = new_todo
            print("New Todo Has Been Saved!")
        case 'complete':
            todo_number = int(input("Select a todo to complete: ")) - 1
            todos.pop(todo_number)
        case "exit":
            break
        case user_error:
            print("This is an invalid input. Try again.")

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