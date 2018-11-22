from MVP1.open_ruby import *
candidate_a_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')

from difflib import SequenceMatcher

def similarites_lignes(code1,code2):
    num = []
    total = 0
    liste_code1=code1.split('\n')
    liste_code2=code2.split('\n')
    for ligne1 in liste_code1:
        if ligne1=="" or "end" in ligne1:
            liste_code1.remove(ligne1)
    for ligne2 in liste_code2:
        if ligne2=="" or "end" in ligne2:
            liste_code2.remove(ligne2)
    for ligne1 in liste_code1:
        for ligne2 in liste_code2:
            num.append(SequenceMatcher(None, ligne1, ligne2).ratio())
    for number in num:
        if number > 0.4:
            total += 1
        point_similar = (total / len(num)) *100
    return 100 - point_similar


print(similarites_lignes(candidate_a_rb, candidate_a_rb))