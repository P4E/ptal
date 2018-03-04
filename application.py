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

syn = wd.synsets("want")
lemmas = set(chain.from_iterable([word.lemma_names() for word in syn]))

translator = gt.Translator()

#translator.translate("Je suis dans la cuisine", dest="en")

stopwords = set('for a of the and to in'.split())






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


model = Word2Vec.load_word2vec_format('/tmpGoogleNews-vectors-negative300.bin', binary=True, norm_only=True)



import gensim

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('C:\\Users\\neth\\git\\ptal\\gv.bin', binary=True)  

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
save_obj(model, "googlewv")


vectcat = model.get_vector("cat")

sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
sentence_president = 'The president greets the press in Chicago'.lower().split()

#from nltk.corpus import stopwords
#nltk.download('stopwords')
#stopwords = nltk.corpus.stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stopwords]
sentence_president = [w for w in sentence_president if w not in stopwords]

distance = model.wmdistance(sentence_obama, sentence_president)