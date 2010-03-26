
numerator = 22*10**1000L                    # 100 digit precision

def get_divided_str(numerator, num):
    return str(numerator/num)

def get_longest_cycle(number, numerator):
    '''Gets the longest recurring cycle in
    numerator/number.'''
    divided_num = get_divided_str(numerator, number)
    digits_dict = {}
    print "divided_num is:", divided_num
    for digit in divided_num:
        try:
            digits_dict[digit] += 1
        except:
            digits_dict[digit] = 1

    print "The dict is:"
    print digits_dict
        


get_longest_cycle(13,numerator)


       
