"""
Read the todo file
and return the list of todos
"""
def get_todos(filepath = "todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_argument, filepath = "todos.txt"):
    """Write the todos in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_argument)