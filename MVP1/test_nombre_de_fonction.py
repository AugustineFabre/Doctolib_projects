def test_nombre_de_fonctions():
    code_a_tester=openRb('/Users/yepmoujj/PycharmProjects/DoctoLib Recruitment/event_candidate_a') ## prend en entrée le code contenant 10 fonctions
    if nombre_fonction(code_a_tester)==10:
        print("fonction validée")
    else:
        print("erreur")

print(test_nombre_de_fonctions())
