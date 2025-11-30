#Create a simple todo list
todos = []

while True:
    user_action = input("Type add/show/edit/exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            print("Saved")
            todos.append(todo)
        case "show":
            print("Saved ToDos:", todos)
        case "edit":
            todo_number = int(input("Select a todo to edit(1 - ...): ")) - 1
            new_todo = input("Enter a new todo: ")
            todos[todo_number] = new_todo
            print("New Todo Has Been Saved!")
        case "exit":
            break
        case user_error:
            print("This is an invalid input. Try again.")

#Replace a symbol in a string

filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentation.txt"]

for i in filenames:
    i = i.replace('.', ')', 1)
    print(i)

# Define a tuple of color codes

color_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))