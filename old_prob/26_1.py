
numerator = 10**100L
testnum = str(625*numerator + numerator/7)

def get_index_list(str_inp, char_current):
    '''Returns a list with all indices of positions of
    the char_current in str_inp.'''

    return [i for i in xrange(0, len(str_inp)) if str_inp[i] == char_current]
    
def main(str_inp):
    main_counter = 0
    # while main_counter < 5:
    char_current = str_inp[main_counter]
    index_list = get_index_list(str_inp, char_current)
    for counter, index_found in enumerate(index_list):
        index_first = index_found
        index_second = index_list[counter + 1]
        index_third = index_list[counter + 2]

        str_first = str_inp[index_first + 1: index_second]
        str_second = str_inp[index_second + 1: index_third]
        if str_first != str_second:
            print "No!"
            continue
        else:
            print "Difference=", len(str_first)

    
def mainx(str_inp):
    main_counter = 0
    # while main_counter < 5:
    char_current = str_inp[main_counter]
    index_list = get_index_list(str_inp, char_current)
    index_skip = 1
    for counter_main, index_found in enumerate(index_list):
        for counter_sub, index_found in enumerate(index_list[counter_main + 1:]):
            index_first = index_found
            index_second = index_list[counter + 1]
            index_third = index_list[counter + 2]

            str_first = str_inp[index_first + 1: index_second]
            str_second = str_inp[index_second + 1: index_third]
            if str_first != str_second:
                print "No!"
                continue
            else:
                print "Difference=", len(str_first)
