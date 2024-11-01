Wordle Solver ASSIST:

Overview
This project is a Python-based Wordle solver that helps players guess the target word in the game Wordle. It uses a filtering algorithm based on user feedback to narrow down the list of possible words.

Features

Starts with words containing unique letters for maximum information.
Adjusts possible words based on user feedback about correct letters (green) and letters in the word but in the wrong position (orange).
Interactive user prompts for easy input.
Requirements
Python 3.x
Two text files:
WordleAnswersList.txt: Contains valid five-letter words for Wordle.
FiveLetterWords.txt: Contains five-letter words with unique letters (optional).

How to Use

Ensure you have Python installed on your machine.

[//]: # (Prepare your word lists:)

[//]: # (Create and populate WordleAnswersList.txt with valid words.)

[//]: # (Optionally, create FiveLetterWords.txt.)

Run the program: 
bash
Copy code
python3 ALGO.py

Follow the prompts to input your guesses and feedback.


Functions

green(greenIndices, possible_words, word_tried): Filters words based on correctly guessed letters.
orange(orangeLetters, possible_words): Filters words based on letters that are in the word but not in the correct position.
ash(ashLetters, possible_words): Filters out words that contain letters confirmed not to be in the word.
License
This project is open source.