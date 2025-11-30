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
            print(todos)
        case "edit":
            todo_number = int(input("Select a todo to edit: "))
            todo_number = todo_number - 1
            new_todo = input("Enter a new todo: ")
            todos[todo_number] = new_todo
            print("New Todo Has Been Saved!")
        case "exit":
            break
        case user_error:
            print("This is an invalid input. Try again.")