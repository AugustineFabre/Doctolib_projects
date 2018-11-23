from MVP1.open_ruby import *
candidate_a_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_b_rb = openRb('../fichier_ruby/event_candidate_b.rb.rb')
candidate_a_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')
candidate_b_rb_test = openRb('../fichier_ruby/event_candidate_b_test.rb.rb')

from MVP2.nom_function import nomFunc
from MVP2.nom_variable import nom_variable
from MVP2.nom_test import nomTest

funcs_a = nomFunc(candidate_a_rb)
funcs_b = nomFunc(candidate_b_rb)

vars_a = nom_variable(candidate_a_rb)
vars_b = nom_variable(candidate_b_rb)

test_a = nomTest(candidate_a_rb_test)
test_b = nomTest(candidate_b_rb_test)

from difflib import SequenceMatcher

def comparison(list_a, list_b):
    num =[]
    total = 0
    for elem_a in list_a:
        for elem_b in list_b:
            num.append(SequenceMatcher(None, elem_b, elem_a).ratio())
    for number in num:
        if number > 0.6:
            total += 1
        point_similar = total / len(num) *100
    return 100 - point_similar


point_simil_func = comparison(funcs_a, funcs_b)
point_simil_vari = comparison(vars_a, vars_b)
point_simil_test = comparison(test_a, test_b)
print(point_simil_test)
print(point_simil_vari)
print(point_simil_func)


