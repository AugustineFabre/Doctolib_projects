from MVP1.open_ruby import openRb
#candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

from MVP2.nom_test import nomTest

def Contenu_test(code):
    liste=nomTest(code)
    print(liste)
    indice_test=input("entrer un nombre correspondant à l'indice du titre: ")
    nom_test=liste[int(indice_test)]
    liste_code=code.split('\n')
    taille=len(liste_code)
    if nom_test in liste:
        for i in range(taille):
            if 'test ' in liste_code[i] and nom_test in liste_code[i]:
                resultat=""
                p=i
                while liste_code[p]!='  end':
                    resultat =resultat+ "\n" +liste_code[p]
                    p +=1
                return resultat+'\n'+'  end'
    else:
        return "erreur"

#print(Contenu_test(candidate_rb_test))