while True:
    #expect the user enter one of the actions
    user_action = input("Type add/show/replace/delete/exit: ").strip()

    if "add" in user_action:
            #expect the user to enter add and todo
            todo = user_action[4:]
            #open a file where this string will be stored and append the string to the end.
            with open("files/todos.txt", "a") as file:
                file.write(todo)

    elif "show" in user_action:
            #open a file and read the content by line
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            #print out the numbered items from the file
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item.capitalize()}")

    elif "replace" in user_action:
        #expect the user to enter replace and index value
        number = int(user_action[8:])
        number = int(number) - 1
        #open a file
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        #expect the user to enter a string for replacement
        new_todo = input("Enter new todo: ") + "\n"

        #save the new string in the same place (index)
        todos[number] = new_todo
        print("New Todo Has Been Saved!")

        #open a file and overwrite the string
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "delete" in user_action:
        #expect the user to enter delete and index value
        number = int(user_action[7:])
        number = int(number) - 1
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        #delete the index by the entered number. number value = index in a string
        todos.pop(number)

        #update the file
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("Invalid input. Try add/show/replace/delete/exit.")