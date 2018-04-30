import sys

import googletrans
from googletrans import Translator

from generePhrase import *


def generateParaphrase(listphrase):
    '''
    input : liste de phrases:
    output : liste de paraphrases
    '''
    
    
    translator = Translator()
    
    chemin1 = ['en', 'es', 'ru', 'fr']
    chemin2 = ['en', 'fi', 'it', 'fr']
    chemin3 = ['en', 'german', 'it', 'fr']
    chemin4 = ['en', 'ar', 'ja', 'zh-cn', 'fr']
    
    chemins = [chemin1, chemin2, chemin3, chemin4]
    
    p = "" 

    
    for x in listphrase:
        p=p+x;
        
        
    
    res = []
    for chemin in chemins:
        temp = p
        for lang in chemin: 
            temp = translator.translate(temp, dest=lang).text
            
        res.append(temp)
        
    return res


def generateParaphrase1(phrase):
    
    '''
        input : une phrase
        output : liste de paraphrase
    '''
    translator = Translator()
    
    chemin1 = ['en', 'es', 'ru', 'fr']
    chemin2 = ['en', 'fi', 'it', 'fr']
    chemin3 = ['en', 'german', 'it', 'fr']
    chemin4 = ['en', 'ar', 'ja', 'zh-cn', 'fr']
    
    chemins = [chemin1, chemin2, chemin3, chemin4]
        
        
    
    res = []
    for chemin in chemins:
        temp = phrase
        for lang in chemin: 
            temp = translator.translate(temp, dest=lang).text
            
        res.append(temp)
        
    return res




#orig = input("Entrez la phrase à paraphraser : ")

#dic = googletrans.LANGUAGES
#l = list(dic.keys())
#print(l)
#chemin = l
#temp = orig
'''
fichier = open(sys.argv[1])
chemin = ['fr', 'es', 'en']

'''
#for line in fichier.readlines():
 #   print("Ligne lue :\n", line)
  #  temp = line
   # for ln in chemin:
    #    temp = translator.translate(temp, dest=ln).text
        #print("Étape "+ln+", traduction : "+temp+", fr : "+ translator.translate(temp, dest='fr').text)
     #   print("\nÉtape "+ln+", retraduite en français : \n"+translator.translate(temp, dest='en').text)




        