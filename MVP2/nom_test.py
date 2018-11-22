from MVP1.open_ruby import *
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')


def nomTest(string):
    Funcs = []

    for line in string.split('\n'):
        if "test " in line:
            index0 = line.index("test ")
            line1 = line[(index0+6):]

            where = line1.index('"')
            nom = line1[:where]

            Funcs.append(nom)
    return Funcs

print(nomTest(candidate_rb_test))