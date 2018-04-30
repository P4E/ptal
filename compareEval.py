# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 04:39:36 2018

@author: dabi-
"""

import matplotlib.pyplot as plt

def compareEvaluation():
    '''
    
    Compare l'evaluation donnée par l'humain avec celui donnée par l'algorithme word2vec complété par la
    distance cosinus
    '''
    f = open("C:\\Users\\dabi-\\git\\ptal\\eval.txt").readlines()
    
    wv = []
    h = []
    import pdb
    for e in f:
    
        l = e.split()
        wv.append(l[0])
        h.append(l[1])
        
    
    plt.scatter(h, wv, color="blue")
    plt.xlabel("human jugement")
    
    plt.show()