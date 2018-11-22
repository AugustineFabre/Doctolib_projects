from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
from MVP2.contenu_fonc.py import *
from MVP1.num_functions import *

def taille_moyenne_fnc(code):
    num_fncs=nombre_fonction(code)
    taille_fncs=[]
    somme=0
    bad=0
    for i in range(num_fncs):
        contenu_fnc=Contenu_fonction(code,i).split('\n')
        taille_fncs.append(len(contenu_fnc))
        somme +=len(contenu_fnc)
    moyenne=somme/len(taille_fncs)
    for i in range(num_fncs):
        if taille_fncs[i]>moyenne:
            if "#" not in Contenu_fonction(code,i):
                bad +=1
    return (1-bad/num_fncs)*100

print(taille_moyenne_fncs(code))
 


point_avoir_comment = taille_moyenne_fnc(candidate_rb)
#print(point_avoir_comment)



#{31: 1, 35: 1, 39: 7, 51: 3, 57: 3, 63: 5, 71: 4, 78: 4, 85: 4, 92: 9}




