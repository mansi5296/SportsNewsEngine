from common import *
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

def getStopword():
    stop_words = set(stopwords.words('english'))
    custom_list = [',', '.', "''", "``", "'", '"', '”', '“', '--', '(', ')']
    for item in custom_list:
        stop_words.add(item)
    return stop_words

def tokenize(words, stop_words):
    word_tokens = word_tokenize(words)
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def convertVector(words):
    word_dict = {}
    
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    
    return word_dict

def process(files, savename):
    stop_words = getStopword()
    term_freq = []
    metadata = []
    document_freq = {}
    for filename in files:
        data = openFile(filename)
        print ("\t" + filename)
        for element in data: 
            print (element)
            word_list = tokenize(element['body'], stop_words)
            for word in word_list:
                if word not in document_freq:
                    document_freq[word] = 0
            vector = convertVector(word_list)
            for key in vector:
                document_freq[key] += 1
            article = {'index' : len(metadata), 'title' : element['title'], 'author' : element['author'], 'date' : element['date']}
            term_freq.append(vector)
            metadata.append(article)
    #return term_freq, all_words
    corpus = {'tf' : term_freq, 'df' : document_freq, 'metadata' : metadata}
    
    writeFile(savename, corpus)

if __name__ == "__main__":
    news_list = ['abcnews.json', 'foxnews.json', 'nbcfootballnews.json', 'nypost.json']
    process(news_list, "corpus_raw.json")
