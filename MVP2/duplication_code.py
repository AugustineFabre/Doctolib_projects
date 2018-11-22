from MVP1.open_ruby import *
candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')

from difflib import SequenceMatcher

def duplicate_code(string):
    num = []
    total = 0
    list_str = string.split('\n')
    for search in list_str:
        if (search != '') and ("end" not in search):
            for line in list_str[list_str.index(search)+1 : ]:
                num.append(SequenceMatcher(None, search, line).ratio())
    for number in num:
        if number > 0.4:
            total += 1
        point_similar = total / len(num) *100
    return 100 - point_similar

print(duplicate_code(candidate_rb))
print(duplicate_code(candidate_rb_test))