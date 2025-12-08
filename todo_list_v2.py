def get_todos():
    with open("files/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos):
    with open("files/todos.txt", "w") as file_local:
        file_local.writelines(todos)

while True:
    #expect the user enter one of the actions in lowercase
    user_action = input("Type add/show/replace/delete/exit: ").strip().lower()

    if user_action.startswith("add"):
            #expect the user to enter add and a string
            todo = user_action[4:]
            #open a file where this string will be stored
            todos = get_todos()

            #check if the todo already exists
            if todo.strip().lower() in [t.strip().lower() for t in todos]:
                print(f"Todo '{todo.strip()}' already exists!")
            else:
                #append the string to the end of the list.
                print(f"Todo '{todo.strip()}' has been added.")
                todos.append(todo + "\n")
                write_todos(todos)

    elif user_action.startswith("show"):
            #open a file and read the content by line
            todos = get_todos()
            #print out the numbered and capitalized items from the file
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item.capitalize()}")

    elif user_action.startswith('replace'):
        try:
            number = int(user_action[8:]) - 1
            #expect the user to enter a string for replacement
            new_todo = input("Enter new todo: ")
            todos = get_todos()

            #save the new string in the same place (index)
            todos[number] = new_todo  + "\n"
            print("New Todo Has Been Saved!")

            #open a file and overwrite the string
            write_todos(todos)

        except ValueError:
            print("Invalid Input! Please try the command again.")
            continue

    elif user_action.startswith('delete'):
        try:
        #expect the user to enter delete and index value
            number = int(user_action[7:])
            number = int(number) - 1
            todos = get_todos()
        #delete the index by the entered number. number value = index in a string
            todos.pop(number)

        #update the file
            write_todos(todos)

        except IndexError:
            print("Invalid Input! The todo with this number does not exist.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid input. Try add/show/replace/delete/exit.")