# Import the json module to work with JSON files
import json

# Open the JSON file 'questions.json' in read mode
with open("questions.json", 'r') as json_file:
    content = json_file.read()  # Read the entire content of the file as a string

# Parse the JSON string into a Python object (list of dictionaries)
data = json.loads(content)

# Initialize counters for correct and incorrect answers
correct_answer = 0
incorrect_answer = 0

# Automatically get the total number of questions from the data
questions = len(data)


# Loop through each question in the data, with an index
for question_index, question in enumerate(data):
    # Print the question number and the question text
    print(f"Question {question_index + 1}) {question['question_text']}")

    # Loop through all alternatives for the current question, with an index
    for index, alternative in enumerate(question['alternatives']):
        # Print each alternative option numbered starting from 1
        print(f"{index + 1}) {alternative}")

    user_answer = int(input("Enter your answer number: "))
    question["user_answer"] = user_answer

    # Check if the user's answer matches the correct answer
    if question["user_answer"] == question["correct_answer"]:
        # If correct, increment the correct_answer counter
        correct_answer = correct_answer + 1
    else:
        # If incorrect, increment the incorrect_answer counter
        incorrect_answer = incorrect_answer + 1

#Compare the user's answers with the correct answers
for question_index, question in enumerate(data):
    message = f"\nQuestion {question_index + 1}: {question['question_text']} \n"\
    f"Your answer: {question['user_answer']}\n"\
    f"Correct answer: {question['correct_answer']}"
    print(message)


# Print the correct and incorrect answers and the final mark
print(f"\nResults:"
f"\nCorrect answers: {correct_answer}/{questions}")

# Calculate and print out the final mark as a percentage
mark = float(correct_answer / questions) * 100
print(f"Your mark: {mark:.2f}%")

#Final mark message
if 90 <= mark <= 100:
    print("Awesome! Keep going!")
elif 80 <= mark < 90:
    print("Great job!")
elif 60 <= mark < 80:
    print("Good effort! Keep practicing!")
elif 40 <= mark < 60:
    print("Not bad, but you can do better!")
else:
    print("Don't worry, try again and you'll improve!")