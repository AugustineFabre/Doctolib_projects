from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')

def nomFunc(string):
    Funcs = []

    for line in string.split('\n'):
        if "def " in line:
            index0 = line.index("def ")
            line1 = line[(index0+4):]

            if "(" in line1:
                index1 = line1.index("(")
                line1 = line1[:index1]

            if "self." in line1:
                index2 = line1.index("self.")
                line1 = line1[(index2+5):]

            Funcs.append(line1)
    return Funcs

print(nomFunc(candidate_rb))
