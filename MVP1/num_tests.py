from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def nombre_test(tests):
    compteur=0
    for i in range (0,len(tests)-3):
        elem1=tests[i]
        elem2=tests[i+1]
        elem3=tests[i+2]
        elem4=tests[i+3]
        liste=elem1+elem2+elem3+elem4
        if liste=="test":
            compteur=compteur+1
    return (compteur)

testCount = nombre_test(candidate_rb_test)

#print(testCount)