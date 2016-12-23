import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction

import random
stopwords = nltk.corpus.stopwords.words('english')
#print stopwords[:10]
'''import sys
reload(sys)
sys.setdefaultencoding('utf8')'''


from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
text = open ("biggboss10","r")
synopses =[]
for line in text:
    line=line.strip()
    if line!='':
        synopses.append(line)

#print synopses[0][:200]

#print len(synopses)

#json.loads(unicode(opener.open(...), "ISO-8859-1"))

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens
'''with open ("biggboss10","r") as f:
    text=f.read()
    text= unicode(text, errors='ignore')
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens1.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens1]

filtered_tokens = []
with open ("biggboss10","r") as f:
    text=f.read()
    text= unicode(text, errors='ignore')
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)'''

def main(tt):
#not super pythonic, no, not at all.
#use extend so it's a big flat list of vocab
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in synopses:
        i = i.decode('utf-8').replace(u'\u014c\u0106\u014d','-')
        allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
        totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)

    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    #print 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame'



    #print totalvocab_stemmed[0]
    '''print vocab_frame.head()
    print
    print
    print
    print'''
    from sklearn.feature_extraction.text import TfidfVectorizer

    #define vectorizer parameters
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,min_df=0.2, stop_words='english',use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) #fit the vectorizer to synopses
    #idf_matrix=tfidf_vectorizer.inverse_transform(synopses)
    #print(tfidf_matrix.shape)



    terms = tfidf_vectorizer.get_feature_names()
    #print type(tfidf_matrix)

    from sklearn.metrics.pairwise import cosine_similarity
    dist = 1 - cosine_similarity(tfidf_matrix)

    from sklearn.cluster import KMeans
    num_clusters = 13
    km = KMeans(n_clusters=num_clusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()


    from sklearn.externals import joblib

    #uncomment the below to save your model 
    #since I've already run my model I am loading from the pickle

    joblib.dump(km, 'doc_cluster.pkl')

    km = joblib.load('doc_cluster.pkl')
    clusters = km.labels_.tolist()



    clus=random.randrange(0, 13)
    strr = " "
    for i in range(len(clusters)):
        if (clusters[i]==clus):
            strr +=  synopses[i]+"\n"

    return strr



