def Contenu_fonction(code):
    liste=nomFunc(code)
    nom_fonction=input('entrer un nom de fonction')
    liste_code=code.split('\n')
    taille=len(liste_code)
    if nom_fonction in liste:
        for i in range(taille):
            if 'def' in liste_code[i] and nom_fonction in liste_code[i]:
                resultat=""
                p=i+1
                while liste_code[p]!='  end\r':
                    resultat =resultat+ "\n" +liste_code[p]
                    p +=1
                return resultat+'\n'+'  end\r'
    else:
        return "erreur"
