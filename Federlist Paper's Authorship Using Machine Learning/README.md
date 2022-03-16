## Objective:
Gain experience in text classification using machine learning with Python and sklearn.
This is a multi-class classification problem. All sklearn classifiers do multiclass classification with
no special parameters required. The do multi-class classification by decomposing the problem
into binary classification problems. Read more in the docs. 

## Background: 
The Federalist Papers is a collection of documents written by Alexander Hamilton,
James Madison, and John Jay collectively under the pseudonym Publius. These documents were
written to persuade voters to ratify the US Constitution. These documents continue to be
influential to this day, as they are frequently cited in Federal court rulings, as well as law blogs,
and political opinions


**FUN FACT:** Many of these essays by Hamilton and Madison were written last minute as both Hamilton and Madison were
extremely busy at this point in their careers. Here is an excerpt from Ron Chernow's biography on Alexander Hamilton, 
"So excruciating was the schedule, Madison said, that often "whilst the printer was putting into type parts of a number, 
the following parts were under the pen and to be furnished in time for the press". Very often, 
Hamilton and Madison first read each other's contributions in print" pg 249

Keep in mind these essays have been cited over 200 times in the Supreme Court. Don't let anyone tell you great
writing can never be done last minute :)

## Overview: 
The data set used is a collection of Federalist Papers from Project Gutenberg. There are 83 documents in this data set which has two columns: one
for the author(s), and one for the text of the document.
The NLP task of authorship attribution is the attempt to identify the author of a document, given
samples of authors' work. In this data set, the breakdown by author is as follows:

• Alexander Hamilton 49

• James Madison 15

• John Jay 5

There are several documents for which authorship is in dispute by historians:

• Hamilton or Madison 11

• Hamilton and Madison 3


