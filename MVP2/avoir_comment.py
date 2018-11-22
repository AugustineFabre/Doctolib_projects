from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')

def taille_moyenne_fnc(code):
    liste_code=code.split('\n')
    taille=len(liste_code)
    s=0
    dic_s1 = []
    dic_s2 = []
    nombre_fonction=0
    bad = 0

    for i in range(taille):
         if 'def ' in liste_code[i]:
             nombre_fonction+=1
             p = i+1
             s1 = 0
             while liste_code[p]!='  end':
                 if ("end" not in liste_code[p]) or (liste_code[p].index("end") != liste_code[i].index("def")):
                     s1 += 1
                 p += 1
             dic_s1.append(i)
             dic_s2.append(s1)
             s += s1
   # print(dic_s1)
    print(dic_s2)
    taille_moy = s/(nombre_fonction)
   # print(taille_moy)

    for i in range(len(dic_s1)):
        if dic_s2[i] > taille_moy and ("#" not in liste_code[dic_s1[i]-1]):
            bad += 1
    return (1-bad/nombre_fonction) *100


point_avoir_comment = taille_moyenne_fnc(candidate_rb)
#print(point_avoir_comment)



#{31: 1, 35: 1, 39: 7, 51: 3, 57: 3, 63: 5, 71: 4, 78: 4, 85: 4, 92: 9}




