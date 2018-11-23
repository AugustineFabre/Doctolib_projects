def nombre_fonction(code):
    compteur=0
    if len(code)>=4:    #pour eviter qu'il y ait une erreur
        for i in range (0,len(code)-3):
            elem1=code[i]
            elem2=code[i+1]
            elem3=code[i+2]
            elem4=code[i+3]
            liste=elem1+elem2+elem3+elem4    
            if liste=="def ":       #on compare 4 caracteres d'affilee 
                compteur=compteur+1
    return (compteur)








