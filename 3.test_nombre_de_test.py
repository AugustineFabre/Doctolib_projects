def test_nombre_de_tests():
    code_a_tester=openRb('/Users/yepmoujj/PycharmProjects/DoctoLib Recruitment/event_candidate_a') ## prends en entrée le code contenant 16 tests
    if nombre_fonction(code_a_tester)==16:
        print("fonction validée")
    else:
        print("erreur")

print(test_nombre_de_tests())
