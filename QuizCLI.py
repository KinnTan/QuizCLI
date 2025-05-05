import os
import json
import random

def get_file():
    file_number = 1
    for files in os.listdir():
        print(str(file_number) + " " + files)
        file_number += 1

    while True:
        try:
            file_index = int(input("Pick the number of your quiz file: "))
        except ValueError:
            print("Please enter a number")
            continue
        if file_index == 0 or file_index > len(os.listdir()):
                print("Number not associated with any file, try again")
        else:
            break

    quiz_file = os.listdir()[file_index - 1]

    if is_json(quiz_file):
        return quiz_file
    else:
        return get_file()

def is_json(quiz_file):
    while not quiz_file.endswith(".json"):
        print("File not a quiz json file, Try Again")
        return False
    else:
        try:
            json.load(open(quiz_file))
        except json.decoder.JSONDecodeError:
            print("File is empty, Try Again")
            return False
        return True

def is_valid_quiz(quiz_data):
    for question_item in quiz_data:
        try:
            (question_item["question"])
        except KeyError:
            return False
        try:
            question_item["choices"]
        except KeyError:
            return False
        try:
            question_item["correct_answer"]
        except KeyError:
            return False
        for choice_letter in question_item["choices"]:
            try:
                (question_item["choices"][choice_letter])
            except KeyError:
                return False
    return True

def main():
    quiz_file = get_file()
    quiz_data = json.load(open(quiz_file))

    while not is_valid_quiz(quiz_data):
        print("Quiz file invalid, Try Again")
        quiz_file = get_file()
        quiz_data = json.load(open(quiz_file))

    # Loads quiz data from JSON file
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