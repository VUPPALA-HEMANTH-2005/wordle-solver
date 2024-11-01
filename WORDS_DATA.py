wordle_answers_file = open('./WordleAnswersList.txt')

wordle_answers = {i[:-1] for i in wordle_answers_file}


def word_with_unique_letters(word):
    st = set()
    for i in word:
        if i in st:
            return False
        else:
            st.add(i)
    return True


unique_wordle_answers = {i for i in wordle_answers if word_with_unique_letters(i)}

wordle_answers_file.close()


