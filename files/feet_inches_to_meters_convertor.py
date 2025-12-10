#importing functions from an external dir, file
from files.parse_function import parse
from files.convert_function import convert

feet_inches = input("Enter feet and inches(example: 4.2): ")

#a cleaner version of variables that store the results of the parse function
parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches = {result:.2f} meters")

if result < 1:
    print(f"{result:.2f} meters. You can't go jumping :/")
else:
    print(f"{result:.2f} meters. You can go jumping! Have fun :D")