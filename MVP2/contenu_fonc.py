from MVP1.open_ruby import openRb
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
from MVP2.nom_function import nomFunc

def Contenu_fonction(code,indice):
    liste=nomFunc(code)
    nom_fonction=liste[indice]
    liste_code=code.split('\n')
    taille=len(liste_code)
    if nom_fonction in liste:
        for i in range(taille):
            if 'def' in liste_code[i] and nom_fonction in liste_code[i]:
                resultat=""
                p=i
                while liste_code[p]!='  end':
                    resultat =resultat+ "\n" +liste_code[p]
                    p +=1
                return resultat+'\n'+'  end'
    else:
        return "erreur"

#print(Contenu_fonction(candidate_rb))
