import sys
import pathlib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random


def preprocess_text(raw_text):
    '''
    Steps
        1. tokenize the lower case raw text, reduce the tokens to only those that are alpha, not in
        the NLTK stopword list, and have length > 5
        2. lemmatize the tokens and use set() to make a list of unique lemmas
        3. do pos tagging on the unique lemmas and print the first 20 tagged items (see the
        pos_NLTK notebook in Part 2 Chapter 6 of the GitHub)
        4. create a list of only those lemmas that are nouns
        5. print the number of tokens (from step a) and the number of nouns (step d)
        6. return tokens (not unique tokens) from step a and nouns from the function
    '''

    # lowercase the raw text
    raw_text = raw_text.lower()

    # tokenize the lower-case raw text
    tokens = word_tokenize(raw_text)

    # a. reducing tokens to only those that are alphas, not in stopword list and have len greater than 5
    tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]

    # b. lemmatize the tokens and use set() to make a list of unique lemmas
    wnl = WordNetLemmatizer()
    tokens = [wnl.lemmatize(t) for t in tokens]
    lemmas_unique = list(set(tokens))

    # c. do pos tagging on the unique lemmas and print the first 20 tagged items (
    tags = nltk.pos_tag(lemmas_unique)
    print("Printing first 20 tagged items", tags[0:20])

    # d. create a list of only those lemmas that are nouns
    nouns = []
    for token, pos in tags:
        if pos == "NN":
            nouns.append(token)

    print("Number of tokens from step a: ", len(tokens))
    print("Number of nouns: ", len(nouns))

    return tokens, nouns


def guessing_game(most_common):
    lives = 5
    random_word_pair = random.choice(most_common)
    random_word = random_word_pair[0]
    print("\nLet's play a word guessing game!")
    #print(random_word)
    board = '_ '*len(random_word)
    guess = ''

    while lives >= 0 and guess != '!':
        print(board)
        guess = input("Guess a letter:")

        if guess == '!':
            print("Exited game.")
            break
        # if user guesses right then add 1 to score and show the letter on the board
        if guess in random_word:
            lives += 1
            print("Right! Your score is ", lives)
            index = []
            board_list = list(board)
            # get the index of the correct guess
            for i in range(0, len(random_word)):
                if random_word[i] == guess:
                    index.append(i)
            # fill in the letter on the board at every index that it appears
            for i in range(len(board)):
                if i in index:
                    board_list[i*2] = guess
            board = "".join(board_list)

            # if there are no underores then the user guessed the whole word
            # genergate new word and keep playing
            if '_' not in board:
                print(board)
                print("You solved it!\n")

                print("Current score: ", lives, '\n')
                print("Guess another word or enter '!' to exit")
                random_word_pair = random.choice(most_common)
                random_word = random_word_pair[0]
                #print(random_word)
                board = '_' * len(random_word)

        # if user guesses wrong subtract score and make sure they are not out of lives
        elif guess not in random_word:
            lives -= 1
            if lives == -1:
                print("Game over! Thanks for playing")
                break
            print("Sorry, guess again. Score is ", lives)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter a file name as system arg: ")
        quit()
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as file:
        # reads in file and split on newline and stores in text_in
        # text in is a list of strings where each string is a line from the file
        text_in = file.read()

    # tokenize text to find lexical diversity
    tokens = word_tokenize(text_in)
    '''
    Note to grader: Finding lexical diveristy is listed before writing the pre-process text function.
    Otherwise, I would not have tokenized the text twice.
    '''
    # find unique tokens to calculate lexical diversity
    unique_tokens = set(tokens)
    num_unique_tokens = len(unique_tokens)
    lexical_diversity = num_unique_tokens / len(tokens)
    print("Lexical diversity: ", round(lexical_diversity, 2))

    # pre-process the text
    all_tokens, only_nouns = preprocess_text(text_in)

    # create dictionary of {noun:count of noun in tokens}
    noun_dict = {t: all_tokens.count(t) for t in only_nouns}

    # using sorted to sort dictonary
    sorted_counts = sorted(noun_dict.items(), key=lambda x: x[1], reverse=True)
    print("Printing 50 most common words and their counts", sorted_counts[0:50])

    # save 50 most common nouns for guessing game
    most_common = []
    for i in range(50):
        most_common.append(sorted_counts[i])

    # play guessing game
    guessing_game(most_common)











