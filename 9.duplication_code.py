from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

def duplicate_code(string):
    num = 0
    list_str = string.split('\n')
    for search in list_str:
        if (search != '') and ("end" not in search):
            for line in list_str:
                if (search in line) and (list_str.index(search) != list_str.index(line)):
                    num +=1
    return num

print(duplicate_code(candidate_rb))
