def taille_moyenne_fnc(code):
    liste_lignes_provisoire=code.split("\n")
    liste_lignes=liste_lignes_provisoire[::-1]
    liste_fonctions=[]
    liste_end=[]
    liste_def=[]
    for i in range (0, len(liste_lignes)):
        if '  end' in liste_lignes[i]:
            liste_end.append(i)
        if 'def ' in liste_lignes[i]:
            liste_def.append(i)
    indices=[]
    j=liste_end[1]
    k=0
    for i in range (0,len(liste_def)):
        while liste_end[k]<liste_def[i] :
            k+=1
        indices.append([j,liste_def[i],liste_end[k]-j])
        if k+1<len(liste_end):
            j=liste_end[k+1]
    s=0
    for element in indices:
        s=element[0]-element[1]-element[2]
    s=s/len(indices)
    return(s)

