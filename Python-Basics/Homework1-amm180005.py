# Homework 1
# Anthony Martinez | amm180005
# 09/03/21

import sys
import pathlib
import re
import pickle

# Creating person class to store employee information
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # will be used to display Person Object after it is stored in dict
    def display(self):
        print('Employee id: ' + self.id)
        print("\t" + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t' + self.phone+'\n')

def process_lines(text_in):

    # will be used to store result of spitting text_in
    text_Split = []

    # The following for loop splits text_in on comma and stores results in a new list called text_Split
    # text_split will be a list of lists where each element is a line from the input file split on commas
    for i in range(0,len(text_in)):
        temp = text_in[i].split(',')
        text_Split.append(temp)

    # dict will store employee id as key and a Person object as value
    dict = {}

    # this for loop will...
    # 1. Modify last and first name to be capital case
    # 2. Modify middle initial to be singe upper case, use 'X' if no letter is present
    # 3. Modify, if needed, id to be two letters followed by 4 digits
    # 4. Modify, if needed, phone number to be in form xxx-xxx-xxxx
    # 5. Store person in dict once their information is validated
    for i in text_Split:

        # modify last name and first name to be capital case
        # index 0 is last name, index 1 is first name
        i[0].capitalize()
        i[1].capitalize()

        # modify middle initial to be a single upper case letter, if necessary. Use ‘X’ as a middle initial if one is missing.
        # index 2 is middle initial
        if i[2] == '':
            i[2] = 'X'
        else:
            i[2] = i[2].upper()

        # modify id using regex. The id should be 2 letters followed by 4 digits
        # 're.match('[a-zA-Z]{2}\d{4}',i[3]) -> checks to make sure first 2 characters are either lower or capital letters
        # and the last 4 characters are digits
        while ((re.match('[a-zA-Z]{2}\d{4}', i[3])) == None):
            print("ID invalid: " + i[3])
            print("ID is two letters followed by 4 digits")
            i[3] = input("Please enter valid id: ")

        # modify phone number, if necessary, to be in form xxx-xxx-xxxx. Use regex
        # 'replace' will be used to check if the 4th and 8th characters are a space, dash, or period
        # and will place a all with a dash
        replace = re.search(r"[\d]{3} |.|-[\d]{3} |.|-[\d]{4}", i[4])
        if replace is not None:
            fixFirst = re.sub(' ', '-', i[4])  # stores phone number after 4th character is replaced with a dash
            fixSecond = re.sub('\.', '-', fixFirst)  # stores phone number after 4th AND 8th character replaced with dash
            i[4] = fixSecond

        # is_ten stores given phone number is 10 digits
        is_ten = re.search(r"[\d]{10}",i[4])
        # if given phone number is 10 digits then insert '-' after first and second 3 digits
        if is_ten is not None:
            add_dash = re.sub(r'(\d\d\d)(\d\d\d)(\d\d\d\d)', r'\1-\2-\3', i[4])
            i[4] = add_dash
        # While not in correct format, prompt user to enter correct format
        while (re.match('\w{3}-\w{3}-\w{4}', i[4]) == None):
            print("Phone " + i[4] + " is invalid ")
            i[4] = input("Enter phone number in form xxx-xxx-xxxx: ")
        # now that data is corrected for the employee, create the person object
        emp = Person(i[0], i[1], i[2], i[3], i[4])

        # Check for duplicate id
        # print an error message if an ID is already in the dict.
        while i[3] in dict:
            print("ID invalid: " + i[3])
            print("ID must be unique")
            i[3] = input("Please enter a valid ID: ")
        # if id is not already in dict then add it to the dict
        else:
            dict[i[3]] = emp
    return dict

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter a file name as system arg: ")
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        # reads in file and split on newline and stores in text_in
        # text in is a list of strings where each string is a line from the csv file
        text_in = f.read().splitlines()

    employees = process_lines(text_in[1:]) # ignore heading line

    # pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read the pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # print employees
    print('\n\nEmployee list:\n')

    for i in employees:
       employees[i].display()








