## Overview
Using a chapter from a medical textbook (located in the file “anat19.txt” in the data folder) parse the chapter and create a database of words. This list of words will be used for a word guessing game. This project served to familiarize myself with **NLTK** and its various functionalities. As well as to perform basic Natural Language Processing techniques such as **data cleaning**. 

## Process
- Read in file as raw text
- Calculate **lexical diversity**
- **Tokenize** the next using *NLTK tokenizer**
- **Preprocess** the data
  - **Tokenize** the lower-case raw text
  - Only tokenizer tokens that are alpha
  - Remove words that are in **NLTK stopwords list**
  - Remove words with more than 5 letters
  - **Lemmatize** the tokens using **NLTK lemmatizer**
  - Create a set of unique lemmas
  - Do **Part of Speech (POS) tagging** on unique lemmas. 
  - Create a list of this lemmas that are nouns
- Create a **database** of words. In this case a dictionary of {noun:count of noun in tokens}
- Sort the dictionary by the 50 most common words that appear in the original file
- These words will be used for the guessing game
- Create a classic **python** word guessing game 
