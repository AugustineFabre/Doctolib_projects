def openRb(filename):
    with open(filename) as f:
        read_data = f.read()
       # print(read_data)
        f.closed
    return read_data

candidate_rb = openRb('../fichier_ruby/event_candidate_a.rb.rb')
candidate_rb_test = openRb('../fichier_ruby/event_candidate_a_test.rb.rb')
print(candidate_rb_test)