
# n -> n/2 ( n is even )
# n -> 3n + 1 ( n is odd )


number_of_terms_dict = {}

def next_term(num_input):
    global number_of_terms_dict
    number_of_terms = 0
    n = num_input
    while 1:
        if n not in number_of_terms_dict:
            number_of_terms += 1
            if n % 2 == 0:
                n = n/2
                yield n
            else:
                n = 3*n + 1
                yield n
            if n == 1:
                number_of_terms_dict[num_input] = number_of_terms
                return
        else:
            number_of_terms += number_of_terms_dict[n]
            number_of_terms_dict[num_input] = number_of_terms
            return


for number in xrange(1,1000001):
    for num in next_term(number):
        pass
    
max_value = 0
max_key = 0

for elem in number_of_terms_dict.iteritems():
    if elem[1]>max_value:
        max_key = elem[0]
        max_value = elem[1]

print max_key, ":", max_value
# for key in number_of_terms_dict:
#     print "Number = ", key, " Terms= ", number_of_terms_dict[key]


