from MVP1.open_ruby import *
candidate_a_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_b_rb = openRb('../fichier_ruby/event_candidate_b.rb.rb')

from MVP2.nom_function import nomFunc
from MVP2.nom_variable import nom_variable

funcs_a = nomFunc(candidate_a_rb)
funcs_b = nomFunc(candidate_b_rb)

vars_a = nom_variable(candidate_a_rb)
vars_b = nom_variable(candidate_b_rb)

def comparison(list_a, list_b):
    num =0
    for elem_a in list_a:
        for elem_b in list_b:
            if elem_a == elem_b:
                num += 1
    return num

similarity_func = comparison(funcs_a, funcs_b)
similarity_vari = comparison(vars_a, vars_b)
