from MVP1.open_ruby import openRb
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

from MVP2.analyse_fonc_var import *
def points_noms(code):
    alpha1, num_meaningful_a1 = seulement_alpha(nom_variable(code))
    alpha2, num_meaningful_a2 = seulement_alpha(nomFunc(code))
    return( (1-(analyse_nom(alpha1,num_meaningful_a1))[0]/len(alpha1))*100 , (1-(analyse_nom(alpha2,num_meaningful_a2))[0]/len(alpha2))*100 )
point_nom_var = points_noms(candidate_rb)[0]
point_nom_fonc = points_noms(candidate_rb)[1]
print(point_nom_var)
print(point_nom_fonc)

from MVP2.case_else import *
point_bon_case = trouver_les_case(candidate_a_rb)
point_bon_case_test = trouver_les_case(candidate_a_test_rb)
print(point_bon_case)
print(point_bon_case_test)

from MVP2.diff_chose_meme_nom import *
point_dif_vari = dif_chose_meme_nom(variables)
point_dif_func = dif_chose_meme_nom(functions)
point_dif_test = dif_chose_meme_nom(tests)
print(point_dif_func)
print(point_dif_test)
print(point_dif_vari)

from MVP2.duplication_code import *
point_dupli_code = duplicate_code(candidate_rb)
point_dupli_test = duplicate_code(candidate_rb_test)
print(point_dupli_code)
print(point_dupli_test)

from MVP2.num_argument import *
point_trop_long = nomFunc(candidate_rb)
print(point_trop_long)

from MVP3.similarite_ligne_par_ligne import *
point_simil_code = similarites_lignes(candidate_rb, candidate_b_rb)
print(point_simil_code)

from MVP3.comparison_variable_fonction import *
point_simil_func = comparison(funcs_a, funcs_b)
point_simil_vari = comparison(vars_a, vars_b)
point_simil_test = comparison(test_a, test_b)
print(point_simil_func)
print(point_simil_test)
print(point_simil_vari)

from MVP2.avoir_comment import *
point_avoir_comment = taille_moyenne_fnc(candidate_rb)
print(point_avoir_comment)



