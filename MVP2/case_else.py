from MVP1.open_ruby import *
candidate_a_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_a_test_rb = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def trouver_les_case(code):
    liste_code = code.split('\n')
    where = []
    num_else = 0

    for line in liste_code:
        if "case" in line:
            index_case = liste_code.index(line)
            for line_apres in liste_code[index_case+1:]:
                if "end" in line_apres:
                    index_end = liste_code.index(line_apres)
                    where.append([index_case, index_end])
    for case in where:
        for line1 in liste_code[case[0]:case[1]]:
            if "else" in line1:
                num_else += 1
    num_case = len(where)
    num_bad = num_case - num_else
    if num_case == 0:
        return 100
    else:
        return (num_else / num_case) * 100

print(trouver_les_case(candidate_a_rb))
print(trouver_les_case(candidate_a_test_rb))



