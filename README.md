# QuizCLI

## Overview

QuizCLI is a command-line quiz runner that reads quiz questions from a JSON file and guides the user through a multiple-choice quiz experience. It includes animations, colored terminal output, a dynamic progress bar, and score reporting at the end. The quiz data must be preformatted and stored as a valid JSON file.

> **To use QuizCLI, you must create your quiz files using [Quiz Builder CLI](https://github.com/KinnTan/quiz_builder_cli).**
> See [Notes](https://github.com/KinnTan/QuizCLI?tab=readme-ov-file#notes) for the example json structure format

## Requirements

* Python 3.x
* No external libraries are required beyond Python’s built-in modules (`json`, `os`, `time`, `random`).

## Installation

**Option 1: Clone the Repository**

```bash
git clone https://github.com/KinnTan/QuizCLI.git
cd quizcli
```

**Option 2: Download from Release**

1. Go to the Releases page.
2. Download the latest `.zip` or `.tar.gz` archive.
3. Extract the archive and navigate into the folder in your terminal.

## Usage

1. Ensure a valid `.json` quiz file is in the same directory.

2. Run the script:

   ```bash
   python quizcli.py
   ```

3. Follow the prompts to select a quiz file and answer multiple-choice questions.

4. Your progress will be shown in a dynamic progress bar, and your final score will be displayed at the end.

### Example Interaction

```
$ python quizcli.py

 ██████╗  ██╗   ██╗ ██╗ ███████╗     ██████╗ ██╗      ██╗
██╔═══██╗ ██║   ██║ ██║ ╚══███╔╝    ██╔════╝ ██║      ██║
██║   ██║ ██║   ██║ ██║   ███╔╝     ██║      ██║      ██║
██║▄▄ ██║ ██║   ██║ ██║  ███╔╝      ██║      ██║      ██║
╚██████╔╝ ╚██████╔╝ ██║ ███████╗    ╚██████╗ ███████╗ ██║
 ╚══▀▀═╝   ╚═════╝  ╚═╝ ╚══════╝     ╚═════╝ ╚══════╝ ╚═╝

Scanning current directory for files...
Files in the Current Directory
1. quiz_data.json
2. another_quiz.json

Enter the number corresponding to your quiz file: 1

Question 1:
What is the capital of France?
a. Madrid
b. Berlin
c. Paris
d. Rome

Your answer: c

Progress: |████████████--------------------------| 3/10 (30%)

...

Quiz Complete! Your final score: 8/10
```

## Notes

* Quiz files must be valid `.json` files with a specific structure:

  ```json
  [
    {
      "question": "What is 2 + 2?",
      "choices": {
        "a": "3",
        "b": "4",
        "c": "5",
        "d": "22"
      },
      "correct_answer": "b"
    }
  ]
  ```
To easily create files in this format, use [Quiz Builder CLI](https://github.com/KinnTan/quiz_builder_cli).

* Files are validated before use, and malformed or non-JSON files will be rejected.
* Users can retry with another quiz or exit the program after completing a quiz.

## Potential Improvements

* Display correct answers after incorrect responses
* Support for timed quizzes
* Improved handling for larger quizzes (pagination or sections)
* Optional sound or audio feedback