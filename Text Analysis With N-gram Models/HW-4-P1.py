import sys
import pathlib
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import pickle

# this function will take in a file, tokenize the text, create unigrams, create bigrams, a bigram dict and unigram dict
def language_model(file_name):
    # a. create function with a filename as argument
    # b. read in the next and remove newlines

    # c. tokenize the text | # e. use nltk to create a unigrams list
    unigrams = word_tokenize(file_name)

    # d. use nltk to create a bigram list
    bigrams = list(ngrams(unigrams, 2))

    # f. use the bigram list to create a bigram dictionary of bigrams and counts, [‘token1 token2’] -> count
    bigrams_dict = {i:bigrams.count(i) for i in set(bigrams)}

    # g. use the unigram list to create a unigram dictionary of unigrams and counts, [‘token’] -> count
    unigrams_dict = {i:unigrams.count(i) for i in set(unigrams)}

    return unigrams_dict, bigrams_dict


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("There must be 3 files sent as sys argv")
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        eng_text = f.read()  # removes newlines
    eng_uni_dict, eng_bi_dict = language_model(eng_text)
    # print(eng_uni_dict, eng_bi_dict)

    rel_path = sys.argv[2]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r', encoding="utf-8",) as f:
        french_text = f.read()  # removes newlines
    fre_uni_dict, fre_bi_dict = language_model(french_text)
    # print(fre_uni_dict, fre_bi_dict)

    rel_path = sys.argv[3]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r', encoding="utf-8", ) as f:
        italian_text = f.read()  # removes newlines
    ita_uni_dict, ita_bi_dict = language_model(italian_text)
    # print(ita_uni_dict, ita_bi_dict)

    # pickle the dictionaries to be read in program 2
    with open('eng_uni_dict.pickle', 'wb') as handle:
        pickle.dump(eng_uni_dict, handle)
    with open('eng_bi_dict.pickle', 'wb') as handleO:
        pickle.dump(eng_bi_dict, handleO)

    with open('fre_uni_dict.pickle', 'wb') as handleT:
        pickle.dump(fre_uni_dict, handleT)
    with open('fre_bi_dict.pickle', 'wb') as handleF:
        pickle.dump(fre_bi_dict, handleF)

    with open('ita_uni_dict.pickle', 'wb') as handleI:
        pickle.dump(ita_uni_dict, handleI)
    with open('ita_bi_dict.pickle', 'wb') as handleS:
        pickle.dump(ita_bi_dict, handleS)
