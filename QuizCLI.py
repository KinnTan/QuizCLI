import os
import time
import json
import random

def display_logo(logo):
    logo_dictionary = {
        "title_logo": """\x1b[38;5;37m\033[01m
         ..|''||   '||'  '|' '||' |'''''||       ..|'''.| '||'      '||' 
        .|'    ||   ||    |   ||      .|'      .|'     '   ||        ||  
        ||      ||  ||    |   ||     ||        ||          ||        ||  
        '|.  '. '|  ||    |   ||   .|'         '|.      .  ||        ||  
          '|...'|.   '|..'   .||. ||......|     ''|....'  .||.....| .||.                                                                                                                                  
            \033[0m
        """,
        "start_logo": """\x1b[38;5;37m
         ██████╗  ██╗   ██╗ ██╗ ███████╗     ██████╗ ██╗      ██╗
        ██╔═══██╗ ██║   ██║ ██║ ╚══███╔╝    ██╔════╝ ██║      ██║
        ██║   ██║ ██║   ██║ ██║   ███╔╝     ██║      ██║      ██║
        ██║▄▄ ██║ ██║   ██║ ██║  ███╔╝      ██║      ██║      ██║
        ╚██████╔╝ ╚██████╔╝ ██║ ███████╗    ╚██████╗ ███████╗ ██║
         ╚══▀▀═╝   ╚═════╝  ╚═╝ ╚══════╝     ╚═════╝ ╚══════╝ ╚═╝
    \033[0m
        """
    }

    print(logo_dictionary[logo])

def loading_animation(duration, message):
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time() # Record the start time to track the duration
    total_frames = len(spinner)  # Number of frames in the spinner
    duration_in_seconds = duration / 1000.0 # Calculate the total time in seconds (allow milliseconds)
    time_per_frame = duration_in_seconds / total_frames # Calculate time per frame to maintain smooth animation
    while True:
        for i in spinner:
            print(f"\r{i} {message}", end="")  # Print the spinner and message on the same line
            time.sleep(time_per_frame)  # Pause briefly to create the animation effect

        # Check if the total elapsed time has exceeded the specified duration
        if time.time() - start_time > duration_in_seconds:
            break
    clear_screen()

def clear_screen():
    os.system('cls')

# Get and validate a quiz file from the current directory
def get_file(error_message=None):
    file_number = 1
    clear_screen()
    display_logo("start_logo")

    if error_message:
        loading_animation(250, "\033[91mError... \x1b[38;5;117m Rescanning current directory for files...")
    else:
        loading_animation(250, "\x1b[38;5;117mScanning current directory for files...")

    clear_screen()
    display_logo("start_logo")

    if error_message is not None:
        print(error_message)

    print("\x1b[38;5;74m\033[01mFiles in the Current Directory\033[0m")
    for files in os.listdir(): # Lists all files in the current directory with numbers
        print(f"\033[97m\033[01m{file_number}. \033[0m\033[093m{files}\033[0m")
        file_number += 1
    try:
        file_index = int(input("\x1b[38;5;74m\033[01mEnter the number corresponding to your quiz file: "))
        if file_index == 0 or file_index > len(os.listdir()):  # Checks if number is within valid range
            return get_file("\033[91m\033[01mThat number doesn't match any file. Please choose a valid number from the list above.\033[0m")
        quiz_file = os.listdir()[file_index - 1]  # Gets the file name based on the user selection

        json_error = validate_json(quiz_file)

        if not json_error:  # Checks if file is a valid JSON
            if is_valid_quiz(json.load(open(quiz_file))):  # Checks the quiz file format
                return quiz_file
            else:
                return get_file("\033[91mThe selected file appears to be malformed. Please choose another file.\033[0m")
        elif json_error:
            return get_file(json_error)
        else:
            return get_file()
    except ValueError:  # Handles non-numeric input
        return get_file("\033[91mInvalid input. Please enter a number.\033[0m")

# Validates the selected file is a proper JSON quiz file
def validate_json(quiz_file):
    # Ensure file ends with .json extension
    if not quiz_file.endswith(".json"):
        return "\033[91mThat is not a JSON file. Please select a file with a .json extension.\033[0m"
    try: # Attempt to load the JSON file
        json.load(open(quiz_file))
    except json.decoder.JSONDecodeError: # Handle empty or invalid JSON
        return "\033[91mThat JSON file is empty or corrupted. Please select a different file.\033[0m"
    return None

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

def progress_bar(quiz_data, progress, bar_length = 50):
    quiz_length = len(quiz_data)
    percentage = progress / quiz_length
    filled_len = int(bar_length*percentage)
    bar = '\x1b[38;5;37m█\033[0m' * filled_len + '\033[97m-' * (bar_length - filled_len)
    print(f"\r\x1b[38;5;74mProgress: \033[97m|{bar}| \x1b[38;5;74m{progress}/{quiz_length} ({percentage*100:.0f}%)\033[0m", flush=True)

def run_quiz(quiz_data):
    correct_answers_counter = 0  # Initialize a counter to track the number of correct answers
    progress = 1
    invalid_letter = False

    while True:
        display_logo("title_logo")
        progress_bar(quiz_data, progress)

        if progress >= len(quiz_data):
            break

        question_item = quiz_data[progress]
        print(f"\n\033[97m{question_item["question"]}\033[0m")
        for choice_letter in question_item["choices"]:  # Loops through each choice option
            print(f"\033[97m\033[01m{choice_letter}. \033[93m{question_item["choices"][choice_letter]}\033[0m")  # Prints the choice letter and its corresponding answer text

        while True:
            if invalid_letter:
                print("\033[91mInvalid letter chosen, Try Again...\033[0m")
                user_response = input("\033[97mYour answer: \033[0m").strip().lower()  # Prompt to input answer
            else:
                user_response = input("\n\033[97mYour answer: \033[0m").strip().lower()  # Prompt to input answer

            if user_response in ["a", "b", "c", "d"]: # Checks if the user's answer matches the correct answer
                invalid_letter = False
                if user_response in question_item["correct_answer"]:
                    correct_answers_counter += 1
                    progress += 1
                    clear_screen()
                    break
                else:
                    progress += 1
                    clear_screen()
                    break
            else:
                clear_screen()
                invalid_letter = True
                break

    score_percentage = correct_answers_counter / len(quiz_data)
    if score_percentage >= 0.8:
        color = "\033[92m"
    elif score_percentage >= 0.5:
        color = "\033[93m"
    else:
        color = "\033[91m"

    loading_animation(300, "\x1b[38;5;37mGetting Results...\x1b[0m...")
    final_score = str(correct_answers_counter) + "/" + str(len(quiz_data))  # format of final_score
    display_logo("start_logo")
    print(f"\x1b[38;5;74mQuiz Complete! Your final score: {color}\033[01m{str(final_score)}\033[0m")
    exit_quiz()

def exit_quiz():
    while True:
        exit_prompt = input("\n\033[96mWould you like to open another quiz?\033[0m \033[93m(Type 't' to retry or 'e' to exit):\033[0m").strip().lower()
        if exit_prompt == "t":
            print("\nExiting current quiz\n")
            main()
            break
        elif exit_prompt == "e":
            print("\033[091m\nExiting QuizCLI...\033[0m")
            exit()
        else:
            print("\033[91mInvalid input. \033[93mPlease enter 't' to try another Quiz or 'e' to exit.\033[0m")

def main():
    clear_screen()
    display_logo("start_logo")

    quiz_data = json.load(open(get_file())) # Get and load quiz file
    loading_animation(300, "\x1b[38;5;37mVerifying quiz file structure...")

    loading_animation(700, "\x1b[38;5;37mQuiz file verified successfully")
    random.shuffle(quiz_data)  # Shuffles the quiz data to randomize question order

    loading_animation(700, "\x1b[38;5;37mStarting the quiz...")
    run_quiz(quiz_data)

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\033[091m\nExiting...\033[0m")