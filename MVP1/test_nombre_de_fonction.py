from nombre_fonction import nombre_fonction
from open_ruby import openRb

code_a_tester=openRb('../fichier_ruby/event_candidate_a.rb.rb') ## prend en entrée le code contenant 10 fonctions
if nombre_fonction(code_a_tester)==10:
    print("fonction validée")
else:
    print("erreur")


