from MVP1.open_ruby import *
candidate_a_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

from MVP2.nom_variable import nom_variable
variables = nom_variable(candidate_a_rb)
from MVP2.nom_function import nomFunc
functions = nomFunc(candidate_a_rb)
from MVP2.nom_test import nomTest
tests = nomTest(candidate_rb_test)

print(variables)

def dif_chose_meme_nom(choses):
    meme = []
    for i in choses:
        where_i = choses.index(i)
        for j in choses[(where_i + 1):]:
            if j == i:
                meme.append(i)
    meme = list(set(meme))
    return (1-len(meme)/len(choses)) * 100

a = dif_chose_meme_nom(variables)
b = dif_chose_meme_nom(functions)
c = dif_chose_meme_nom(tests)

print(dif_chose_meme_nom(variables))
print(b)
print(c)
