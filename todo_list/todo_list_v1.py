while True:
    #expect the user enter one of the actions
    user_action = input("Type add/show/replace/delete/exit: ").strip()

    #check the action. match if success, print out the error if wrong input
    match user_action:
        case "add":
            #expect the user enters a string
            todo = input("Enter a todo: ") + "\n"
            #open a file where this string will be stored and append the string to the end.
            with open("files/todos.txt", "a") as file:
                file.write(todo)

        case "show":
            #open a file and read the content by line
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            #print out the numbered items from the file
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")

        case "replace":
            #open a file
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            #expecet the user to enter the index value
            number = int(input("Select a todo to replace (1 - ...): ")) - 1

            #expect the user to enter a string for replacement
            new_todo = input("Enter new todo: ") + "\n"

            #save the new string in the same place (index)
            todos[number] = new_todo
            print("New Todo Has Been Saved!")

            #open a file and overwrite the string
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "delete":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            #expect the integer for the index
            number = int(input("Select a todo to delete: ")) - 1
            #delete the index by the entered number. number value = index in a string
            todos.pop(number)

            #update the file
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break

        case _:
            print("Invalid input.")