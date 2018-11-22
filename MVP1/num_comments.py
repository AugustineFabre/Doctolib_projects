from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def nombre_commentaire(code):
    compteur=0
    for caractere in code:
        if caractere=="#":
            compteur=compteur+1
    return compteur

commentCount = nombre_commentaire(candidate_rb)
test_commentCount = nombre_commentaire(candidate_rb_test)

print(commentCount)
#print(test_commentCount)