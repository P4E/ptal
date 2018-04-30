# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 03:45:33 2018

@author: dabi-
"""




import nltk
import numpy as np

#nltk.download('punkt')




def getRandomText():
    
    path = "C:\\Users\\dabi-\\git\\ptal\\data\\"
    filenumber = np.random.randint(11)
    
    f = open("C:\\Users\\dabi-\\git\\ptal\\data\\"+str(filenumber)+".txt").read()
    
    sentances = nltk.sent_tokenize(f)
    
    start = np.random.randint(len(sentances)-3)
    res = sentances[start:start+3]
    
    return res
    