import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import random
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
import json

# used a dictionary of dictionaries to store user data like so
'''
name: {"prefer fiction": fiction, "genre" : [], "recommended books" : []}
'''
user_database = {}

# loading knowledge bases which are list of books but genre
non_fic_knowledge_base = pickle.load(open('knowledge bases/non_fiction_knowledge_base.pickle', 'rb'))
fic_knowledge_base = pickle.load(open('knowledge bases/fiction_knowledge_base.pickle', 'rb'))
fiction_generes = ['choose your own adventure', 'christmas books', 'gothic fiction', 'inspiring novels',
                       'longest fiction novels', 'mystery novels', 'crime novels', 'poetry', 'science fiction', 'world war 1 novels'
                       , 'zombie novels']
non_fiction_generes = ['advertising', 'archeology', 'autobiographies', 'black history', 'energy', 'environmental',
                       'jazz/jazz history', 'kites', 'negotiation', 'popular-physics', 'psychedelics', 'self help',
                       'skepticism', 'world war 2', 'books written by CEOs']

words = []
classes = []
documents = []
punct = ['?', '!', '-', '.']
data_file = open('intents.json').read()
intents = json.loads(data_file)

# appending i and tag to documents which is a list of tuples of (word, what the word is related to)
for intent in intents['intents']:
    for pattern in intent['patterns']:
        i = nltk.word_tokenize(pattern)
        words.extend(i)
        documents.append((i, intent['tag']))

        # make a classes list with all the tags from intents.json
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# use nltk to lemmatize the words and lowercase
lemmas = [lemmatizer.lemmatize(w.lower()) for w in words if w not in punct]
lemmas = sorted(list(set(lemmas)))
classes = sorted(list(set(classes)))

# save words and classes
pickle.dump(words,open('words.pickle','wb'))
pickle.dump(classes,open('classes.pickle','wb'))


'''
Begin training the model
'''
training = []
temp = [0] * len(classes)
for doc in documents:
    bag = [] # bag of words
    pattern_words = doc[0] # doc stores the word and related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    row = list(temp)
    row[classes.index(doc[1])] = 1
    training.append([bag, row])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Done Creating training data")

# create neural network model
# using relu, cateogorical_crosstropy and sgd
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

history = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5)
model.save('AI_model.h5', history)
print("Model Successfully Created!")
print("BOT has entered the chat\n")


intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pickle','rb'))
classes = pickle.load(open('classes.pickle','rb'))
model = load_model('AI_model.h5')

def process_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def vector(sentence, words):
    sentence_words = process_sentence(sentence)
    bag = [0]*len(words)
    for word in sentence_words:
        for i,w in enumerate(words):
            if w == word:
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence, model):
    prob = vector(sentence, words)
    result = model.predict(np.array([prob]))[0]
    threshold = 0.25
    results = [[i,r] for i,r in enumerate(result) if r>threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def bot_response(ints, intents_json):
    tag = ints[0]['intent']
    intents = intents_json['intents']
    for i in intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def bot_answer(text):
    ints = predict_class(text, model)
    flag = None
    tag = ints[0]['intent']
    if tag == 'recommend':
        user_input = input('Do you prefer fiction or non-fiction?')

        if user_name not in user_database:
            user_database[user_name] = {}
            user_database[user_name]['books'] = []
            user_database[user_name]['genre'] = []

        while (flag==None):
            if user_input == 'fiction':
                user_database[user_name]['preference'] = 'fiction'
                print("Here are fiction genres", fiction_generes)
                genre_selection = input("What genre interest you? (Type as shown)")
                while genre_selection not in fic_knowledge_base:
                    genre_selection = input("Try again: ")
                user_database[user_name]['genre'].append(genre_selection)
                recommendation_list = fic_knowledge_base[genre_selection]
                recommendation = random.choice(recommendation_list)
                user_database[user_name]['books'].append(recommendation)

                flag = True
                return "Here is my book recommendation from that genre: " + recommendation
            elif user_input == 'non-fiction':
                user_database[user_name]['preference'] = 'non-fiction'

                print("Here are non-fiction genres", non_fiction_generes)
                genre_selection = input("What genre interest you? (Type as shown)")
                while (genre_selection not in non_fic_knowledge_base):
                    genre_selection = input("Try again: ")
                user_database[user_name]['genre'].append(genre_selection)
                recommendation_list = non_fic_knowledge_base[genre_selection]
                recommendation = random.choice(recommendation_list)
                # make sure it is a new recommendation
                while recommendation in user_database[user_name]:
                    recommendation = random.choice(recommendation_list)
                user_database[user_name]['books'].append(recommendation)
                flag = True
                return "Here is my book recommendation from that genre: " + recommendation
            else:
                user_input = input("Sorry did you say fiction or non-fiction?")
    elif tag == 'goodbye':
        # pickle the user data dictionary
        with open('user_database.pickle', 'wb') as handle:
            pickle.dump(user_database, handle)

        result = bot_response(ints, intents)
        print(result)
        exit()

    result = bot_response(ints, intents)
    return result



# read in user database
user_database = pickle.load(open('user_database.pickle', 'rb'))

# start bot
user_name = input ("BOT: Hello, I am a bot that can recommend books based on your preferences. What is your name?").lower()
if user_name in user_database:
    print("Oh, Hello again "+user_name)
    print("Here is your information from last time")
    print(user_database[user_name])
    user_input = input()
    while (True):
        response = bot_answer(user_input)
        print(response)
        user_input = input()

else:
    print("BOT: Hello, ", user_name + '\n')
    user_input = input("")

    while (True):
        response = bot_answer(user_input)
        print(response)
        user_input = input()



