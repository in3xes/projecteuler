
# Take the number 192 and multiply it by each of 1, 2, and 3:

#         192 * 1 = 192
#         192 * 2 = 384
#         192 * 3 = 576

#                 By concatenating each product we get the 1 to 9
#                 pandigital, 192384576. We will call 192384576 the
#                 concatenated product of 192 and (1,2,3)

#                 The same can be achieved by starting with 9 and
#                 multiplying by 1, 2, 3, 4, and 5, giving the
#                 pandigital, 918273645, which is the concatenated
#                 product of 9 and (1,2,3,4,5).

#                 What is the largest 1 to 9 pandigital 9-digit number
#                 that can be formed as the concatenated product of an
#                 integer with (1,2, ... , n) where n > 1?
                
import number_op

def check_valid_num(num):
    '''Check if given number is worth
    multiplying.'''

    digits_in_num = [0] * 10             # 0-9
    
    for digit in number_op.digits(num):

        if digit == 0:
            return False

        if digits_in_num[digit] > 0:
            return False
        else:
            digits_in_num[digit] += 1

    return True

def get_digits_if_valid(num):
    '''Check if given number is worth
    multiplying.'''

    digits_in_num = [0] * 10             # 0-9
    
    for digit in number_op.digits(num):

        if digit == 0:
            return None

        if digits_in_num[digit] > 0:
            return None
        else:
            digits_in_num[digit] += 1

    return digits_in_num
        
    
def multiply_check_pandigital(num):
    
    if check_valid_num(num):
        conc_string = ''
        product_digits = [0] * 10
        for n in xrange(1,10):
            product = num * n
            #print "product=", product
            try:
                for counter, digit in enumerate(get_digits_if_valid(product)):
                    #print "digit=", digit, "counter=", counter,
                    #print "product_digits=", product_digits
                    if digit > 0 and product_digits[counter] == 1:
                        return n, conc_string
                                        
                    else:
                        product_digits[counter] += digit
            except TypeError:           # None type returned
                return n, conc_string
            conc_string = conc_string + str(product)

        return n, conc_string

    else:
        return 0, '0'

def main():
    max_cat = 0
    max_num = 0
    for i in xrange(10000, 1, -1):
        #for i in xrange(1, 10000):   Use if all are needed
        #print "i=", i
        n, conc_str =  multiply_check_pandigital(i)
        conc_int = int(conc_str)
        if conc_int > max_cat:
            max_cat = conc_int
            max_num = i
        if len(conc_str) == 9:
            break
            print i, "gives", conc_str,"for multiplication upto", n, "."

    print "Maximum concatenated pandigital product is", max_cat, "for", max_num, "."


#print multiply_check_pandigital(793)
if __name__=="__main__":
    main()
            
