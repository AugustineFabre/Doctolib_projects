from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def nombre_fonction(code):
    compteur=0
    for i in range (0,len(code)-2):
        elem1=code[i]
        elem2=code[i+1]
        elem3=code[i+2]
        liste=elem1+elem2+elem3
        if liste=="def":
            compteur=compteur+1
    return (compteur)

functionCount = nombre_fonction(candidate_rb)
test_functionCount = nombre_fonction(candidate_rb_test)

print(functionCount)
#print(test_functionCount)