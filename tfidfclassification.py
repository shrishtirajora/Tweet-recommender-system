from sip import setapi
setapi("QDate", 2)
setapi("QDateTime", 2)
setapi("QTextStream", 2)
setapi("QTime", 2)
setapi("QVariant", 2)
setapi("QString", 2)
setapi("QUrl", 2)
import ast
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import sys

def blah(str_inp):
    print str_inp
    reload(sys)
    sys.setdefaultencoding('utf-8')
    porter = PorterStemmer()
    stop_words = set(stopwords.words("english"))  # load stopwords
    tag = open("hashtags.txt","r")
    text = open("tweet_text_lower.txt","r")
    from collections import defaultdict
    distict_terms= defaultdict(int)
    hash_tags= defaultdict(int)

    count =-1
    ht_index_dict = {}
    ht_index_list = []
    x_size =0
    count  = 0
    with open("hashtags.txt","r") as f:
        
        x=[]
        for line in f:
            x.append(ast.literal_eval(line.strip()))
        
        for ht in x:
            x_size+=1
            ht_str = ""
            for ele in ht:
                ht_str+= str(ele)
            if ht_str in ht_index_dict:
                ht_index_list.append(ht_index_dict[ht_str])
            else:
                ht_index_dict[ht_str] = count;
                count+=1
                ht_index_list.append(ht_index_dict[ht_str])
                
            if(x_size == 1197):
                break
        
    # print ("x_size"+str(x_size))

    #print x
        
        #count =-1
        #for a in x:
        #    for t in a:
        #        if t.lower() not in hash_tags:
        #            count+=1
        #            hash_tags[t.lower()]=count'''

    tagsize=count

    #dictionary of terms
    count =-1
    with open("tweet_text_lower.txt", "r") as f:
        for rec in f:
            for word in rec.split():
                # print word
                if word[0]!='#':
                    if word.strip() not in stop_words:
                        # print word.strip()
                        if porter.stem_word(word.strip()) not in distict_terms:
                            count+=1
                            distict_terms[porter.stem_word(word.strip())]=count
                        
    # print f
    dictsize=count
    # print len(distict_terms), count
    #dictionary of hashtags
    # print len(hash_tags), count

    count=0
    count2 =0
    line_num=0
    with open("tweet_text_lower.txt","r") as f:
            for i, l in enumerate(f):
                pass
            line_num=i+1

    mat = [[0]*(dictsize+1) for i in range(1197)]#replace by line_num+1 
    # mat = [[0]]
    # print mat
    # print  text
    for (line , i) in zip(text, range(1197)):
        # print line
        for word in line.split():
            #print word
            if (word[0]!='#'):
                if word.strip() not in stop_words:
                    #for tags in ast.literal_eval(hash_.strip()):
                        #print distict_terms[word] + hash_tags[tags]
                        mat[i][distict_terms[porter.stem_word(word.lower())]]+=1

    #print mat
    document_freq = [0]*(dictsize+1)
    #print document_freq

    for i in distict_terms:
        for j in range(1197):
            if mat[j][distict_terms[i]]>=1:
                document_freq[distict_terms[i]]+=1

    #print line_num
    #print document_freq
    #for t in distict_terms:
    #    if distict_terms[t]==1:
    #        print t
    #print tagsize
    #print len(distict_terms)
    import math
    for i in distict_terms:
        for j in range(1197):
            mat[j][distict_terms[i]]=math.log(1+mat[j][distict_terms[i]])*(math.log((1197)/(document_freq[distict_terms[i]]+1)))
            #print mat[distict_terms[i]][hash_tags[j]]




    import numpy as np
    import matplotlib.pyplot as plt

    from sklearn.datasets import make_multilabel_classification
    from sklearn.multiclass import OneVsRestClassifier
    from sklearn.svm import SVC
    from sklearn.preprocessing import LabelBinarizer
    from sklearn.decomposition import PCA
    from sklearn.cross_decomposition import CCA
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import MultiLabelBinarizer
    from scipy import spatial
    import numpy as np


    from sklearn.metrics.pairwise import cosine_similarity


    # print line_num


    clf= KNeighborsClassifier(n_neighbors=4)
    #mat = CCA(n_components=2).fit(mat, x).transform(mat)
    #print feature
    #clf = OneVsRestClassifier(SVC(kernel='poly'))
    #mat=np.array(mat)
    #print  len(x)
    #print len(mat)
    #print x[0]

    #test =["not"]*1197
    #print test
    clf.fit(mat, ht_index_list)

    #print type(mat), type(Y)

    query=[0]*(dictsize+1)
    for word in str_inp.split():
        if word[0]!='#':
            if word not in stop_words:
                if porter.stem_word(word) in distict_terms:
                    query[distict_terms[porter.stem_word(word)]]+=1

    for word in distict_terms:
        query[distict_terms[word]]=math.log(1+query[distict_terms[word]])*(math.log((1197)/(document_freq[distict_terms[word]]+1)))

    res_index = clf.predict(query)
    # print res_index

    for key in ht_index_dict:
        if(ht_index_dict[key] == res_index[0]):
            print key
            break

    return key


