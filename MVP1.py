def nombre_fonction(code):
    compteur=0
    for i in range (0,len(code)-2):
        elem1=code[i]
        elem2=code[i+1]
        elem3=code[i+2]
        liste=elem1+elem2+elem3
        if liste=="def":
            compteur=compteur+1
    return (compteur)


code="frdef njii codef"






