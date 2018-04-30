# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:40:18 2018

@author: 3603138
"""


from tools import *
import os.path
import numpy as np
import gensim


def sentance2vec(sentance, model):
    
    try:
        vect = model[sentance[0]]
    except:
        vect = np.zeros(100)
    for i in range(1,len(sentance)):
        try:
            vect+=model[sentance[i]]
        except:
            a=4
        
    return vect


path = "/users/Etu8/3603138/M1S2/TAL/TAL/movies1000/"

alltxts = [] # init vide
labs = []
cpt = 0
for cl in os.listdir(path): # parcours des fichiers d'un répertoire
    print(cl)
    for f in os.listdir(path+cl):
        txt = open(path+cl+'/'+f, "r").read()
        alltxts.append(txt)
        labs.append(cpt)

    cpt += 1
    
    



from nltk.tokenize import RegexpTokenizer




tokenizer = RegexpTokenizer(r'\w+')

alltxts = [g.replace("\n", " ") for g in alltxts]

for i in range(len(alltxts)):
    alltxts[i]=tokenizer.tokenize(alltxts[i])


model = gensim.models.Word2Vec(alltxts)





for i in range(len(alltxts)):
   alltxts[i]=sentance2vec(alltxts[i], model)

alltxts = np.array(alltxts)
labs = np.array(labs)

ind = np.arange(len(alltxts))
np.random.shuffle(ind)

alltxts = alltxts[ind]
labs = labs[ind]

from nltk.stem.snowball import FrenchStemmer
from sklearn.feature_extraction.text import CountVectorizer

stemmer = FrenchStemmer()
analyzer = CountVectorizer().build_analyzer()


from  sklearn.naive_bayes import MultinomialNB



count_vect = CountVectorizer(max_features = 10000, analyzer = analyzer)
x_tf = count_vect.fit_transform(alltxts)



'''
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(norm='l1', use_idf=False).fit(x_count)
x_tf = tf_transformer.transform(x_count)
'''

x_train = x_tf[0:1500]
x_test = x_tf[1500:]

y_train = labs[0:1500]
y_test = labs[1500:]

tr = alltxts[0:1500]
ytr = labs[0:1500]



from sklearn import svm

clf = svm.SVC()
clf.fit(tr, ytr)  

g = nb.predict(x_test)


nbok = 0;

for i in range(len(g)):
    
    if g[i]==y_test[i]:
        nbok+=1;
        
        
score = nbok/len(y_test)


print(score)

