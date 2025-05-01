import json

quiz_data = json.load(open("sample_quiz.json"))  # Loads quiz data from JSON file

for question_item in quiz_data: # Loops through each question in the quiz data
    print(question_item["question"])
    for choice_letter in question_item["choices"]:  # Loops through each choice option
        print(choice_letter + ". " + question_item["choices"][choice_letter])   # Prints the choice letter and its corresponding answer text

    user_response = input("Enter the correct choice: ") # Prompt to input answer

    # Checks if the user's answer matches the correct answer
    if user_response == question_item["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect!")