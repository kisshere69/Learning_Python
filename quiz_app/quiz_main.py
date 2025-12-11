# Import the json module to work with JSON files
import json

# ----------- Load JSON with error handling ------------
try:
    with open("questions.json", "r") as json_file:
        content = json_file.read()
except FileNotFoundError:
    print("Error: questions.json not found!")
    exit()

#Parse JSON safely to avoid incorrect JSON file syntax, structure.
try:
    data = json.loads(content)
except json.JSONDecodeError:
    print("Error: questions.json contains invalid JSON!")
    exit()

# ------------ Initialize counters ---------------
correct_answer = 0
incorrect_answer = 0

# Automatically get the total number of questions from the data
questions = len(data)

# ------------ Main quiz loop --------------------
for question_index, question in enumerate(data):

    # Print the question number and the question itself
    print(f"Question {question_index + 1}) {question['question_text']}")

    # Loop through answer_option for the current question, with an index
    for index, answer_option in enumerate(question['answer_option']):
        print(f"{index + 1}) {answer_option}")

    #Error handling
    while True:
     try:
        user_answer = int(input("Enter your answer number: "))

        if user_answer < 1 or user_answer > len(question["answer_option"]):
            print("Invalid choice! Choose an existing answer number.")
            continue
        break

     except ValueError:
        print("Invalid input. Please enter a number.")

    question["user_answer"] = user_answer

    #Check if the user's answer matches the correct answer
    if question["user_answer"] == question["correct_answer"]:
        correct_answer = correct_answer + 1
    else:
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