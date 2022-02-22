from bs4 import BeautifulSoup
import requests
import re
from urllib.request import Request, urlopen
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import pickle


starter_url = "https://en.wikipedia.org/wiki/Charles_Bukowski"
r = requests.get(starter_url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# trying to scrape from these sites results in various 400 errors so I exclueded them per Dr. Mazidi
do_not_vist = ["http://www.poetryfoundation.org/bio/charles-bukowski", "http://bukowskilive.com/riot_pur.htm",
               "http://brianoverland.com/2014/03/16/writing-in-california-bukowski-vs-moody/","http://www.bu.edu/today/campus-life/2009/03/25/hanging-with-bukowski-gotlieb-center",
               "http://www.wormwoodreview.com/bukowski.html","https://www.eifelzeitung.de/redaktion/kinder-der-eifel/charles-bukowski-134540/"
               ]

# webcralwer
counter = 1
with open('urls.txt', 'w') as f:
    for link in soup.find_all('a'):
        if counter <40:
            link_str = str(link.get('href'))
            #print(link_str)
            if 'Bukowski' in link_str or 'bukowski' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    #print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str and link_str not in do_not_vist:
                    f.write(link_str + '\n')
                    counter+=1
print("end of crawler")

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

def scrape_all_text(urls):
    '''
    function scrapes all text from the urls and outputs it to its own file
    '''
    counter = 1
    for i in range(len(urls)):
        url = urls[i]
        html = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        text = soup.get_text()
        result_file = open("url_text"+str(counter)+".txt", "w+", encoding="utf-8")
        counter+=1
        result_file.write(text)
        result_file.close()
    print("Done scraping text from urls")

def clean_text(urls):
    '''
    function cleans the text in the url_text files and ouputs the clean text to a new text file
    cleaning = remove newlines, lowercase all words, remove stopwords, and tokenize using nltk sent tokenizer
    '''
    count = 1
    for i in range(len(urls)):
        old_file = open("url_text"+str(count)+".txt", "r", encoding="utf-8")
        raw_text = old_file.read()
        text = raw_text.lower()
        old_file.close()
        cleaned_file = open("cleaned_url_text"+str(count)+".txt", "w+", encoding="utf-8")
        tokens = sent_tokenize(text)
        stop_words = set(stopwords.words('english'))
        for i in range(len(tokens)):
            tokens[i] = tokens[i].replace('\n', ' ')
            tokens[i] = re.sub(r'[.?!,:;()&/{}\-\n]', '', tokens[i])
        for i in range(len(tokens)):
            tokens[i] = " ".join([t for t in tokens[i].split() if not t in stop_words and len(t) > 1])
        for i in tokens:
            cleaned_file.write(i+'\n')
        cleaned_file.close()
        count += 1
    print("Done cleaning original files")


def get_important_words(urls):
    ten_words = ["bukowski", "charles", "poetry", "poems", "stories", "work", "story", "life", "writing", "time"]
    knowledge_base = {}
    for word in ten_words:
        knowledge_base[word] = []
    dict = {}
    for i in range(len(urls)):
        cleaned_file = open("cleaned_url_text" + str(i+1) + ".txt", "r", encoding="utf-8")
        lines = cleaned_file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word in dict:
                    dict[word] = dict[word] + 1
                else:
                    dict[word] = 1
        for sentence in lines:
            for word in ten_words:
                if word in sentence:
                    knowledge_base[word] = sentence
    important_words = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:25]
    print("\nImportant words:", important_words)
    print("Knowledge base: ", knowledge_base)

    print("pickling the knowledge base for part 2 of the project")
    # pickle the knowledge base dict for next part of the project
    with open('knowledge_base.pickle', 'wb') as handle:
        pickle.dump(knowledge_base, handle)



# get urls to pass into functions
with open('urls.txt', 'r', encoding="utf-8") as f:
    urls = f.read().splitlines()

scrape_all_text(urls)
clean_text(urls)
get_important_words(urls)



