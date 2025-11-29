todos = []
while True:
    user_action = input("Type add/show/exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            print("Saved")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
        case user_error:
            print("This is an invalid input. Try again.")