from open_ruby import openRb
from nombre_test import nombre_test


code_a_tester=openRb('../fichier_ruby/event_candidate_a_test.rb.rb') ## prends en entrée le code contenant 16 tests
if nombre_test(code_a_tester)==16:
    print("fonction validée")
else:
    print("erreur")
