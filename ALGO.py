from WORDS_DATA import wordle_answers, unique_wordle_answers
import random

possible_words = list(wordle_answers)

attempts = set()


def green(greenIndices, possible_words, word_tried):
    search_space_modification = []
    for ind in greenIndices:
        currLetter = word_tried[ind]
        for word in possible_words:
            if word[ind] == currLetter:
                search_space_modification.append(word)
        possible_words = search_space_modification
        search_space_modification = []
    return possible_words


def orange(orangeLetters, possible_words):
    search_space_modification = []
    for letter in orangeLetters:
        for word in possible_words:
            if letter in word:
                search_space_modification.append(word)
        possible_words = search_space_modification
        search_space_modification = []
    return possible_words


def ash(ashLetters, possible_words):
    search_space_modification = []
    for letter in ashLetters:
        for word in possible_words:
            if letter not in word:
                search_space_modification.append(word)
        possible_words = search_space_modification
        search_space_modification = []
    return possible_words


for iterations in range(6):
    if iterations == 0: # for first attempts choosing from words with unique letters gives more information
        word_tried = random.choice(list(unique_wordle_answers))
    else:
        if not possible_words:
            print("No possible words left. Exiting.")
            break

        word_tried = random.choice(possible_words)
        limit = 1
        while word_tried in attempts and limit < 100:
            word_tried = random.choice
            limit += 1

    print(word_tried)
    attempts.add(word_tried)
    if_won = input('Did you win? (y if won else n) : ')

    if len(possible_words) == 1:
        print(f'{possible_words[0]} is the answer !!!')
        break

    if if_won == 'y' or if_won == 'Y':
        print(f'so {word_tried} is the word !!')
        break  # if won no need to continue further



    isGreen = input('Is Green Present (Enter y if present else n)\n')
    orangeLetters = []
    greenLetters = []

    if isGreen.lower() == 'y':
        greenIndices = list(map(int, input('Give space separated indices (0 indexing)\n').split()))
        greenLetters = [word_tried[i] for i in greenIndices]

        new_search_space = green(greenIndices, possible_words, word_tried)
        possible_words = new_search_space

    isOrange = input('Is Orange Present (Enter y if present else n)\n')
    if isOrange.lower() == 'y':
        orangeLetters = input('Give space separated (orange) letters ').split()
        new_search_space = orange(orangeLetters, possible_words)
        possible_words = new_search_space

    found_letters = greenLetters + orangeLetters

    ashLetters = []
    for letter in word_tried:
        if letter not in found_letters:
            ashLetters.append(letter)

    new_search_space = ash(ashLetters, possible_words)
    possible_words = new_search_space

    # Debugging print to check possible words after filtering
    # print(f'Possible words remaining: {possible_words}')
