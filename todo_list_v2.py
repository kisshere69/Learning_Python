#define the read function with a parameter
def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

#define the write function with a parameter
def write_todos(filepath, todos_argument):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_argument)

while True:
    #expect the user enter one of the actions
    user_action = input("Type add/show/replace/delete/exit: ").strip().lower()

    if user_action.startswith("add"):
            #expect the user to enter add and a string
            todo = user_action[4:]

            #open a file where this string will be stored
            todos = get_todos("files/todos.txt")

            #check if the todo already exists
            if todo.strip().lower() in [t.strip().lower() for t in todos]:
                print(f"Todo '{todo.strip()}' already exists!")

            else:
                #append the string to the end of the list.
                print(f"Todo '{todo.strip()}' has been added.")
                todos.append(todo + "\n")
                write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
            #open a file and read the content by line
            todos = get_todos("files/todos.txt")

            #print out the numbered and capitalized items from the file
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item.capitalize()}")

    elif user_action.startswith('replace'):
        try:
            number = int(user_action[8:]) - 1
            #expect the user to enter a string for replacement
            new_todo = input("Enter new todo: ")
            todos = get_todos("files/todos.txt")

            #save the new string in the same place (index)
            todos[number] = new_todo  + "\n"
            print("New Todo Has Been Saved!")

            #open a file and overwrite the string
            write_todos("files/todos.txt", todos)

        except ValueError:
            print("Invalid Input! Please try the command again.")
            continue

    elif user_action.startswith('delete'):
        try:
        #check the input
            number = int(user_action[7:])
            todos = get_todos("files/todos.txt")
            todo_to_delete = todos[number - 1].strip()

        #delete the index by the entered number. number value = index in a string
            todos.pop(number - 1)
            print(f"Todo '{todo_to_delete}' has been deleted.")

        #update the file
            write_todos("files/todos.txt", todos)

        except IndexError:
            print("Invalid Input! The todo with this number does not exist.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid input. Try add/show/replace/delete/exit.")