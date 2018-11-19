def nombre_fonction(tests):
    compteur=0
    if len(tests)>=4:
        for i in range (0,len(tests)-3):
            elem1=tests[i]
            elem2=tests[i+1]
            elem3=tests[i+2]
            elem4=tests[i+3]
            liste=elem1+elem2+elem3+elem4
            if liste=="test":
                compteur=compteur+1
    return (compteur)

