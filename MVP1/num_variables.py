from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')

def nombre_variable(code):
    compteur=0
    liste_ligne=code.split("\n")
    for ligne in liste_ligne:
        if "def " in ligne:
            if "(" in ligne:
                if "()" not in ligne:
                    for caractere in ligne:
                        if caractere == ",":
                            compteur+=1
                    compteur+=1
        if "def" not in ligne:
            for i in range (0, len(ligne)-2):
                n1=ligne[i]
                n2=ligne[i+1]
                n3=ligne[i+2]
                mot=n1+n2+n3
                if mot==' = ':
                    if "'" not in ligne[0 :i+1]:
                        compteur+=1
        if '|' in ligne:
            compteur+=1
    return compteur

variableCount = nombre_variable(candidate_rb)

#print(variableCount)