todos = []
while True:
    user_action = input("Type add/show/exit: ")
    user_action = user_action.strip()

    match user_action:
        case