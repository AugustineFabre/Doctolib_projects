def openRb(filename): ## prend en entrée le chemin permettant d'accéder au fichier
    with open(filename) as f:
        read_data = f.read()
       # print(read_data)
        f.closed
    return read_data ## renvoie le code de type string

candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')
#print(candidate_rb_test)

