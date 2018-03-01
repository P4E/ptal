import sys

import googletrans
from googletrans import Translator

translator = Translator()

#chemin = ['en', 'ru', 'it', 'de', 'fr']
#orig = input("Entrez la phrase à paraphraser : ")

#dic = googletrans.LANGUAGES
#l = list(dic.keys())
#print(l)
#chemin = l
#temp = orig

fichier = open(sys.argv[1])
chemin = ['fr', 'es', 'en']
for line in fichier.readlines():
    print("Ligne lue :\n", line)
    temp = line
    for ln in chemin:
        temp = translator.translate(temp, dest=ln).text
        #print("Étape "+ln+", traduction : "+temp+", fr : "+ translator.translate(temp, dest='fr').text)
        print("\nÉtape "+ln+", retraduite en français : \n"+translator.translate(temp, dest='en').text)

