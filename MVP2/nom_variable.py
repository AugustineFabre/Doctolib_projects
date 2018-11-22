from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')


def nom_variable(code):
    liste_variable=[]
    liste_ligne=code.split("\n")
    for ligne in liste_ligne:
        if "def " in ligne:
            if "(" in ligne:
                if "()" not in ligne:
                    for i in range (0,len(ligne)):
                        if ligne[i]=="(":
                            n1=i
                        if ligne[i]==")":
                            n2=i
                    liste_intermediaire=ligne[n1+1:n2].split(',')
                    for element in liste_intermediaire:
                        if "=" in element:
                            for i in range (0,len(element)):
                                if element[i]=="=":
                                    n=i
                            liste_variable.append(element[0:n-1])
                        else:
                            liste_variable.append(element)
        if "def" not in ligne:
            for i in range (0, len(ligne)-2):
                n1=ligne[i]
                n2=ligne[i+1]
                n3=ligne[i+2]
                mot=n1+n2+n3
                if mot==' = ':
                    if "'" not in ligne[0:i]:
                        variable=ligne[0:i]
                        liste_variable.append(variable)
        if '|' in ligne:
            n1=0
            n2=0
            for i in range (0,len(ligne)):
                if n1==0:
                    if ligne[i]=="|":
                        n1=i
                if n1!=0:
                    if ligne[i]=="|":
                        n2=i
            liste_variable.append(ligne[n1+1:n2])
    liste_variable=[a.replace(" ","") for a in liste_variable]
    liste_variable=[a.replace("self.","") for a in liste_variable]
    return(liste_variable)

print(nom_variable(candidate_rb))