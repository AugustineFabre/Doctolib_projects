def similarites_lignes(code1,code2):
    index=0
    liste_code1=code1.split('\n')
    liste_code2=code2.split('\n')
    for ligne1 in liste_code1:
        if ligne1=="\r":
            liste_code1.remove(ligne1)
    for ligne2 in liste_code2:
        if ligne2=="\r":
            liste_code2.remove(ligne2)
    for ligne1 in liste_code1:
        for ligne2 in liste_code2:
            if ('end' not in ligne1) and ligne1==ligne2:
                index +=1
    return index
