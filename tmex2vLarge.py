# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:51:07 2018

@author: 3603138
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:12:50 2018

@author: 3603138
"""

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


from tools import *
import os.path
import numpy as np
import nltk


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

path = "/tmp/reviewmovie/"

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
    
    


alltxts = [g.replace("\n", " ") for g in alltxts]

for i in range(len(alltxts)):
    alltxts[i]=tokenizer.tokenize(alltxts[i])


 
sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
#sentences = MySentences('/some/directory') # a memory-friendly iterator
model = gensim.models.Word2Vec(alltxts)

import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_components=2).fit_transform(X)
X_embedded.shape




model.most_similar(positive=['woman', 'king'], negative=['man'], topn=5)
model.most_similar(positive=['woman', 'hero'], negative=['man'], topn=5)


model.most_similar(positive=['woman', 'bad'], negative=['man'], topn=5)


model.most_similar(positive=['french', 'actor'])

model.most_similar(positive=['woman', 'actor'], negative=['man'], topn=5)
model.most_similar(positive=['great'], negative = ["italy"])
 
model.accuracy('questions-words.txt')


import random


films = random.sample(range(0,25000), 100)
word = random.sample(range(0,50), 20)

listword = list()
for f in films:
    for w in word:
        try:
            listword.append(model[alltxts[f][w]])
        except:
            print("not in vocabulary")
            

lw = np.array(listword)


cat = model['cat']
dog = model['dog']
actor = model['actor']
actress = model['actress']
man= model['man']
woman = model['woman']
king = model['king']
queen = model['queen']

X = np.array([cat, dog, actor, actress, man, woman, king, queen])


tr = np.concatenate((X, lw))




xemb = TSNE(n_components=2).fit_transform(tr)

allx = xemb[:,0]
ally = xemb[:,1]

plt.scatter(allx, ally, color="black")
plt.scatter(allx[0:2], ally[0:2], color="red", label="cat dog")
plt.scatter(allx[2:4], ally[2:4], color="green", label="actor actress")
plt.scatter(allx[4:6], ally[4:6], color="yellow", label="man woman")
plt.scatter(allx[6:8], ally[6:8], color="violet", label="king queen")
plt.title("TSNE sur des mots tirés du corpus")
plt.legend()
import matplotlib.pyplot as plt
plt.scatter(xemb[0], xemb[1], color="blue", label="cat dog")
plt.scatter(xemb[2], xemb[3], color="yellow", label="actor actress")
plt.scatter(xemb[4], xemb[5], color="green", label="man woman")
plt.scatter(xemb[4])
plt.show()



import sys
import numpy as np
import matplotlib.pyplot as plt

# définition du nuage

fig, ax = plt.subplots()
coll = ax.scatter(allx, ally, color="black")
# aspects esthétiques facultatifs
#plt.grid(True)
#plt.axis([-0.5, 0.5, -0.5, 0.5])

# défintion du callback: interaction hyperfacile par variables globales !!!
def on_pick(event):
    print(testData[event.ind], "clicked") # récupération auto de l'élément cliqué
    coll._facecolors[event.ind,:] = (1, 0, 0, 1) # modif du plot
    coll._edgecolors[event.ind,:] = (1, 0, 0, 1)
    fig.canvas.draw()

# connection du système
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()


import sys
import numpy as np
import matplotlib.pyplot as plt

# définition du nuage

fig, ax = plt.subplots()
coll = ax.scatter(allx, ally, picker = 1981, s=[50]*len(allx))
# aspects esthétiques facultatifs
plt.grid(True)


# défintion du callback: interaction hyperfacile par variables globales !!!
def on_pick(event):
    #print(allx[event.ind], "clicked") # récupération auto de l'élément cliqué
    coll._facecolors[event.ind,:] = (1, 0, 0, 1) # modif du plot
    coll._edgecolors[event.ind,:] = (1, 0, 0, 1)
    fig.canvas.draw()

# connection du système
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()