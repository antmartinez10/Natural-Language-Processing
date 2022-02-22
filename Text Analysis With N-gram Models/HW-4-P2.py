import pickle
from nltk import word_tokenize
from nltk.util import ngrams

# this function will calculate the probability that a text is of a language using Laplace smoothing
def compute_prob(text, unigram_dict, bigram_dict, v):
    unigram_test = word_tokenize(text)
    bigram_test = list(ngrams(unigram_test,2))

    p_laplace=1
    for bigram in bigram_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d =unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace = p_laplace * ((n+1) / (d + v))

    return p_laplace


if __name__ == '__main__':

    # read in LangId.test file
    with open('data/LangId.test', 'r') as f:
        test_file = f.read().splitlines()  # removes newlines

    # read in pickled dictionaries
    with open('eng_uni_dict.pickle', 'rb') as handle:
        eng_uni = pickle.load(handle)
    with open('eng_bi_dict.pickle', 'rb') as handle:
        eng_bi = pickle.load(handle)
    with open('fre_uni_dict.pickle', 'rb') as handle:
        fre_uni = pickle.load(handle)
    with open('fre_bi_dict.pickle', 'rb') as handle:
        fre_bi = pickle.load(handle)
    with open('ita_uni_dict.pickle', 'rb') as handle:
        ita_uni = pickle.load(handle)
    with open('ita_bi_dict.pickle', 'rb') as handle:
        ita_bi = pickle.load(handle)

    # v is total size of vocabulary. Will be used to compute probabillity
    v = len(eng_uni) + len(fre_uni) + len(ita_uni)
    # this file will be used to write the results
    file = open("results.text", "w+")
    counter = 1
    # this for loop will calculate the prob of each language
    # it will find the highest prob of the three languages and write which language corresponds to that probability
    # to a file called "results.text"
    for i in test_file:
        eng_prob = compute_prob(i, eng_uni, eng_bi, v)
        fre_prob = compute_prob(i, fre_uni, fre_bi, v)
        ita_prob = compute_prob(i, ita_uni, ita_bi, v)

        highest = max(eng_prob,fre_prob,ita_prob)
        if highest == eng_prob:
            file.write(str(counter)+" English\n")
            counter = int(counter)
            counter += 1
        elif highest == fre_prob:
            file.write(str(counter)+" French\n")
            counter = int(counter)
            counter += 1
        else:
            file.write(str(counter)+" Italian\n")
            counter = int(counter)
            counter += 1
    file.close()

    with open('data/LangId.sol') as answers:
        # lines is a list where each element is a line from the text
        answer_lines = answers.read().splitlines()

    with open("results.text") as my_answers:
        my_answer_lines = my_answers.read().splitlines()

    # will store number of correct classification to calculation accuracy percentage
    correct = 0
    # list will be used to store the line number of any incorrect classifications
    line_num_of_incorrect = []

    # this for loop will compare this programs answers to the answer key
    # it will keep track of the number of correct classifications and the line number of any incorrect classifications
    for i in range(0, len(my_answer_lines)):
        if answer_lines[i] == my_answer_lines[i]:
            correct += 1
        else:
            line_num_of_incorrect.append(i)

    accuracy = correct/len(answer_lines)
    print("Accuracy: ", accuracy)
    print("Line number of incorrect classifications: ", line_num_of_incorrect)






