# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:24:00 2018

@author: 3603138
"""


from itertools import chain
from nltk.corpus import wordnet as wd
import nltk
from tkinter import *
import pickle

nltk.download("wordnet")

syn = wd.synsets("want")
lemmas = set(chain.from_iterable([word.lemma_names() for word in syn]))

translator = gt.Translator()

#translator.translate("Je suis dans la cuisine", dest="en")

stopwords = set('for a of the and to in'.split())


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




from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank
import numpy 

b = Word2Vec(brown.sents())
mr = Word2Vec(movie_reviews.sents())
t = Word2Vec(treebank.sents())
 
b.most_similar('money', topn=5)


t.most_similar('money', topn=5)

 
b.most_similar('great', topn=5)

mr.most_similar('great', topn=5)

t.most_similar('great', topn=5)

 
b.most_similar('company', topn=5)

mr.most_similar('company', topn=5)

t.most_similar('company', topn=5)

from nltk.corpus import stopwords


words = brown.sents()[0]
filtered_words = [word for word in words if word not in stopwords.words('english')]

cosine_similarity = numpy.dot(model['spain'], model['france'])/(numpy.linalg.norm(model['spain'])* numpy.linalg.norm(model['france']))




import gensim

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('gv.bin', binary=True)  



def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
save_obj(model, "googlewv")


def meanvec(listvec):
    
    v = listvec[0]

    for i in range(1,len(listvec)):
        v+=listvec[i]
        
    v = v/len(listvec)
    
    return v
    

vectcat = model.get_vector("cat")

sentence_obama = 'the cat is black'.lower().split()
sentence_president = 'the feline is black'.lower().split()

#from nltk.corpus import stopwords
#nltk.download('stopwords')
#stopwords = nltk.corpus.stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stopwords]
sentence_president = [w for w in sentence_president if w not in stopwords]


def sentance2vec(sentence):
    
    vect = list()
    for s in sentence:
        try:
            vect.append(model.get_vector(s))
        except:
            print("")
        
    return np.array(vect)
    
sentence_obama = 'The cat is black and climb the wall'.lower().split()
sentence_president = 'The feline is black and is on the wall'.lower().split()

#from nltk.corpus import stopwords
#nltk.download('stopwords')
#stopwords = nltk.corpus.stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stopwords]
sentence_president = [w for w in sentence_president if w not in stopwords]

print(distancePhrase(sentence_obama, sentence_president))

def distancePhrase(p1, p2):
    
    v1 = sentance2vec(p1)
    v2 = sentance2vec(p2)
    
    m1 = meanvec(v1)
    m2  = meanvec(v2)
    
    return np.dot(m1, m2)/(np.linalg.norm(m1)* np.linalg.norm(m2))    
    

distance = model.wmdistance(sentence_obama, sentence_president)
print(distance)


sentence_obama = 'the cat is black and climb the small wall'.lower().split()
sentence_president = 'the feline is black and climb the wall'.lower().split()

#from nltk.corpus import stopwords
#nltk.download('stopwords')
#stopwords = nltk.corpus.stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stopwords]
sentence_president = [w for w in sentence_president if w not in stopwords]


from nltk.translate.bleu_score import sentence_bleu

sentence_obama = 'The cat is black and climb the wall'.lower().split()
sentence_president = 'The feline is black and is on the wall'.lower().split()

reference = [sentence_obama]
candidate = sentence_president
score = sentence_bleu(reference, candidate)
print(score)