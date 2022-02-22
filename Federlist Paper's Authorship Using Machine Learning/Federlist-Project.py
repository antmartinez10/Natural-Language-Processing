'''
1.
- Read in the csv file using pandas.
- Convert the author column to categorical data.
- Display the first few rows.
- Display the counts by author
'''
import pandas as pd

# Read in the csv file using pandas.
df = pd.read_csv('federalist.csv')

# Convert the author column to categorical data.
df['author'] = df.author.astype('category')
print(df.dtypes)

# Display the first few rows.
print(df.head())

# Display the counts by author

'''
2. 
- Divide into train and test, with 80% in train. Use random state 1234. 
- Display the shape of train and test.
'''
# Set up x and y
X = df.text
y = df.author

# Divide into train and test, with 80% in train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=1234)

# Display the shape of train and test
print("\nShape of the training set before pre-processing text", X_train.shape)
print("Shape of the test set before pre-processing text", X_test.shape)

'''
3. 
- Process the text by removing stop words and performing tf-idf vectorization
- fit to the training data only, and applied to train and test. 
- Output the training set shape and the test set shape
'''

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# removing stopwords
stopwords = set(stopwords.words('english'))
vectorizer = TfidfVectorizer(stop_words=stopwords)

# apply tfidf vectorizer
X_train = vectorizer.fit_transform(X_train)  # fit and transform the train data
X_test = vectorizer.transform(X_test)        # transform only the test data

# output training set shape and test set shape
print("\nShape of the training set after processing", X_train.shape)
print("Shape of the test set after processing", X_test.shape)

'''
4. 
- Try a Bernoulli Naïve Bayes model. 
- What is your accuracy on the test set?
'''

# Building a Bernoulli Naive Bayes model
from sklearn.naive_bayes import BernoulliNB

naive_bayes = BernoulliNB()
naive_bayes.fit(X_train, y_train)

# evaluate on test data
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
pred = naive_bayes.predict(X_test)

# confustion matrix
print(confusion_matrix(y_test,pred))

# accuracy
print("Acc: ", accuracy_score(y_test, pred))

'''
5. 
The results from step 4 are disappointing. The classifier just guessed the predominant class, Hamilton, 
every time. Looking at the train data shape above, there are 7876 unique words in the vocabulary. 
This may be too much, and many of those words may not be helpful. 

- Redo the vectorization with max_features option set to use only the 1000 most frequent words. 
- In addition to the words, add bigrams as a feature. 
- Try Naïve Bayes again on the new train/test vectors and compare your
results. 
'''

# redo vectorization with max_features set to 1000 most frequent words
vectorizer_b = TfidfVectorizer(stop_words=stopwords,max_features=1000,min_df=2,max_df=.5,ngram_range=(1,2))

X = vectorizer_b.fit_transform(df.text) # WHY DOES ADDING VECTORIZER_B HERE MAKE IT WORK?
y = df.author

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=1234)

naive_bayes2 = BernoulliNB()
naive_bayes2.fit(X_train,y_train)

pred2 = naive_bayes2.predict(X_test)
print(confusion_matrix(y_test,pred2))
print("accuracy score for second model: ", accuracy_score(y_test,pred2))

'''
6. 
- Try logistic regression. 
- Adjust at least one parameter in the LogisticRegression() model to see if you can 
improve results over having no parameters. What are your results?
'''

X = df.text
y = df.author

# divide into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=1234)

X_train = vectorizer_b.fit_transform(X_train)  # fit and transform the train data
X_test = vectorizer_b.transform(X_test)        # transform only the test dat

from sklearn.linear_model import LogisticRegression
glm1 = LogisticRegression()
glm1.fit(X_train, y_train)

# Evaluate on test data
pred_log_reg_1 = glm1.predict(X_test)
print("Accuracy for logistic regression model with no parameters: ", accuracy_score(y_test,pred_log_reg_1))

# Building 2nd logistic regression model adding additional parameters in order to imporve results
# multi class specifies multiple classes
# the ibfgs solver is a good choice for multiclass problems which is the case we have here.
glm2 = LogisticRegression(multi_class='multinomial', solver='lbfgs', class_weight='balanced')
glm2.fit(X_train, y_train)
pred_log_reg_2 = glm2.predict(X_test)

print("Accuracy for logistic regression model with parameters ", accuracy_score(y_test,pred_log_reg_2))


'''
Try a neural network. Try different topologies until you get good results. What is
your final accuracy?
'''

# set x and y
X = vectorizer_b.fit_transform(df.text)
y = df.author

# test train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=1234)

from sklearn.neural_network import MLPClassifier
nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100), max_iter=1000, random_state=1)
nn.fit(X_train, y_train)
pred_nn = nn.predict(X_test)
print("Neural Network 1 accuracy ", accuracy_score(y_test,pred_nn))

nn2 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,2), max_iter=1000, random_state=1)
nn2.fit(X_train, y_train)
pred_nn2 = nn2.predict(X_test)
print("Neural Network 2 accuracy ", accuracy_score(y_test,pred_nn2))

nn3 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(4,3), max_iter=1000, random_state=1)
nn3.fit(X_train, y_train)
pred_nn3 = nn3.predict(X_test)
print("Neural Network 3 accuracy ", accuracy_score(y_test,pred_nn3))

nn4 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100,75,50,25,5,2), max_iter=1000, random_state=1)
nn4.fit(X_train, y_train)
pred_nn4 = nn4.predict(X_test)
print("Neural Network 4 accuracy ", accuracy_score(y_test,pred_nn4))

