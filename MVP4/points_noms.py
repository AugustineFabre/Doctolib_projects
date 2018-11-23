def points_noms(code):

    alpha1, num_meaningful_a1 = seulement_alpha(nom_variable(code))
    alpha2, num_meaningful_a2 = seulement_alpha(nom_fonction(code))
    return( (analyse_nom(alpha1,num_meaningful_a1))[1]/len(alpha1)*100 , (analyse_nom(alpha2,num_meaningful_a2))[1]/len(alpha2)*100 )
