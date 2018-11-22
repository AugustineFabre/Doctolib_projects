from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')

def nomFunc(string):
    Funcs = []
    trop_long = 0
    lines = string.split('\n')
    for line in lines:
        if "def " in line:
            if "(" in line:
                index0 = line.index("(")
                index1 = line.index(")")
                para = line[(index0 + 1):index1]
                para = para.split(",")
                if len(para) > 3:
                    trop_long += 1

    return (1 - trop_long / len(lines)) *100

#print(nomFunc(candidate_rb))