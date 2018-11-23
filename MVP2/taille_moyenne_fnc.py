def taille_moyenne_fnc(code):
    liste_code=code.split('\n') #on cree une liste des lignes
    taille=len(liste_code)
    s=0
    nombre_fonction=0
    for i in range(taille):
         if 'def ' in liste_code[i]:
             nombre_fonction+=1
             p=i+1
             while liste_code[p]!='  end':   #on parcourt les lignes a partir d'un def jusqu'a trouver un end, et on compte les lignes
                 if '   end' in liste_code[p]:
                     p=p+1
                 else:
                     s=s+1
                     p +=1

    return s/(nombre_fonction)
