import os
import json
import random

# Get and validate a quiz file from the current directory
def get_file():
    file_number = 1
    for files in os.listdir(): # Lists all files in the current directory with numbers
        print(str(file_number) + " " + files)
        file_number += 1

    while True: # Prompts user until they pick a valid file number
        try:
            file_index = int(input("Pick the number of your quiz file: "))
        except ValueError: # Handles non-numeric input
            print("Please enter a number")
            continue
        if file_index == 0 or file_index > len(os.listdir()): # Checks if number is within valid range
                print("Number not associated with any file, try again")
        else:
            break

    # Gets the file name based on the user selection
    quiz_file = os.listdir()[file_index - 1]

    if is_json(quiz_file): # Checks if file is a valid JSON
        if is_valid_quiz(json.load(open(quiz_file))): # Checks the quiz file format
            return quiz_file
        else:
            print("Quiz file invalid, Try Again")
            return get_file()
    else:
        return get_file() # Retry selection if not valid

# Validates the selected file is a proper JSON quiz file
def is_json(quiz_file):
    # Ensure file ends with .json extension
    while not quiz_file.endswith(".json"):
        print("File not a quiz json file, Try Again")
        return False
    else:
        try: # Attempt to load the JSON file
            json.load(open(quiz_file))
        except json.decoder.JSONDecodeError: # Handle empty or invalid JSON
            print("File is empty, Try Again")
            return False
        return True

# Check if the JSON data contains a valid quiz structure
def is_valid_quiz(quiz_data):
    for question_item in quiz_data:
        try: # Checks if "question" key exists
            (question_item["question"])
        except KeyError:
            return False
        try: # Checks if "choices" key exists
            question_item["choices"]
        except KeyError:
            return False
        try: # Checks if "correct_answer" key exists
            question_item["correct_answer"]
        except KeyError:
            return False
        for choice_letter in question_item["choices"]: # Checks if all choice keys are valid
            try:
                (question_item["choices"][choice_letter])
            except KeyError:
                return False
    return True

def main():
    quiz_data = json.load(open(get_file())) # Get and load quiz file

    random.shuffle(quiz_data)  # Shuffles the quiz data to randomize question order
    correct_answers_counter = 0  # Initialize a counter to track the number of correct answers

    for question_item in quiz_data:  # Loops through each question in the quiz data
        print(question_item["question"])
        for choice_letter in question_item["choices"]:  # Loops through each choice option
            print(choice_letter + ". " + question_item["choices"][
                choice_letter])  # Prints the choice letter and its corresponding answer text

        user_response = input("Enter the correct choice: ")  # Prompt to input answer

        # Checks if the user's answer matches the correct answer
        if user_response == question_item["correct_answer"]:
            correct_answers_counter += 1
            print("Correct!")
        else:
            print("Incorrect!")

    final_score = str(correct_answers_counter) + "/" + str(len(quiz_data))  # format of final_score
    print("Your final score is " + str(final_score))

main()