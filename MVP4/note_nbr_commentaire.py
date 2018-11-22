def note_nbr_commentaire(code):
    nb_commentaire=nombre_commentaire(code)
    taille=taille_moyenne_fnc(code)
    nb=nombre_fonction(code)
    if nb_commentaire==0:
        if taille>5:
            return -20
        else:
            return 0
    else:
        if nb*taille/nb_commentaire>5:
            return -20
        else:
            return 0


