## Overview
In this project I created **bigram** and **unigram** dictionaries for English, French, and Italian using the provided **training data** where the key is the unigram or bigram text and the value is the count of that unigram or bigram in the data. Then for the test data, **calculate probabilities** for each language and compare against the true labels. 

## Program 1: Building Language Model the 3 Languages
- a. create a function with a filename as argument
- b. read in the text and remove newlines
- c. **tokenize** the text
- d. use **nltk** to create a bigrams list
- e. use **nltk** to create a unigrams list
- f. use the bigram list to create a bigram dictionary of bigrams and counts, [‘token1
token2’] -> count
- g. use the unigram list to create a unigram dictionary of unigrams and counts,
[‘token’] -> count
- h. return the unigram dictionary and bigram dictionary from the function
- i. in the main body of code, call the function 3 times for each training file, **pickle**
the 6 dictionaries and save to files with appropriate names. The reason we are
pickling them in one program and unpickling them in another is that NLTK
ngrams is slow and if you put this all in one program you will waste a lot of time
waiting for ngrams() to finish.


## Program 2: 
- a. Read in pickled dictionaries.
- b. For each line in the test file, **calculate a probability for each language** and write the language with the highest probability to a file.
- c. Compute and output your accuracy as the percentage of correctly classified
instances in the test set. The file LangId.sol holds the correct classifications.
- d. Output accuracy, as well as the line numbers of the incorrectly classified items
