def Contenu_test(code):
    liste=nomTest(code)
    print(liste)
    indice_test=input("entrer un nombre correspondant à l'indice du titre")
    nom_test=liste[indice_test]
    liste_code=code.split('\n')
    taille=len(liste_code)
    if nom_test in liste:
        for i in range(taille):
            if 'test ' in liste_code[i] and nom_test in liste_code[i]:
                resultat=""
                p=i
                while liste_code[p]!='  end\r':
                    resultat =resultat+ "\n" +liste_code[p]
                    p +=1
                return resultat+'\n'+'  end\r'
    else:
        return "erreur"
