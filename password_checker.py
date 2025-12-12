'''
#A simple password checker

while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
        continue
    else:
        if password.isnumeric():
            print("Password must contain at least one letter.")
            continue
        elif password.islower():
            print("Password must contain at least one uppercase letter.")
            continue
        elif password.isupper():
            print("Password must contain at least one lowercase letter.")
            continue
        else:
            print("Password is strong. Good job!")
            break
'''
#A password checker with feedback

password = input("Enter your password: ")
#result = []
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isnumeric():
        digit = True

result["Digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Uppercase"] = uppercase

lowercase = False
for i in password:
    if i.islower():
        lowercase = True

result["Lowercase"] = lowercase
print(result)

if all(result.values()):
    print("Strong password. Good job!")
else:
    print("Weak password. Try again.")