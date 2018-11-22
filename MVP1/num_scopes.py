from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def nombre_requetes_SQL(code):
    index = 0
    for ligne in code.split('\n'):
        if "scope " in ligne:
            index += 1
    return index

#print(nombre_requetes_SQL(candidate_rb))