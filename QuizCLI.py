import json
import random

quiz_data = json.load(open("sample_quiz.json"))  # Loads quiz data from JSON file
random.shuffle(quiz_data) # Shuffles the quiz data to randomize question order
correct_answers_counter = 0 # Initialize a counter to track the number of correct answers

for question_item in quiz_data: # Loops through each question in the quiz data
    print(question_item["question"])
    for choice_letter in question_item["choices"]:  # Loops through each choice option
        print(choice_letter + ". " + question_item["choices"][choice_letter])   # Prints the choice letter and its corresponding answer text

    user_response = input("Enter the correct choice: ") # Prompt to input answer

    # Checks if the user's answer matches the correct answer
    if user_response == question_item["correct_answer"]:
        correct_answers_counter += 1
        print("Correct!")
    else:
        print("Incorrect!")

final_score = str(correct_answers_counter) + "/" + str(len(quiz_data)) # format of final_score
print("Your final score is " + str(final_score))