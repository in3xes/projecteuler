
##########################################################################
# Find the number of non-empty subsets of {1^(1), 2^(2), 3^(3),...,      #
# 250250^(250250)}, the sum of whose elements is divisible by 250. Enter #
# the rightmost 16 digits as your answer.                                #
##########################################################################

from math import *
import cPickle as pickle

def get_modulo_list_actual(N, num):
    """Returns a list giving counts of a number modulo num from 1 to N.

    1 -> 251 -> 501 -> 751 ...
    For 1:
    ------
    1^1 (mod 250)
    251^1 = (250 + 1) = 1^1 (mod 250)
    251^2 = 251*1 (mod 250)
    ...
    251^251 = x (mod 250)
    501^251 = (250 + 251)^251 = 250^251 (mod 250)
    ...
    501^501 = y (mod 250)
    ..

    Similarly for 2, 3,..."""

    modulo_list = [0]*num

    for base_num in xrange(1, 250):
        current_exp = 1
        int_num = base_num
        for current_num in xrange(base_num, 250251, num):
        
            while current_exp != current_num:
                int_num = (int_num * base_num) % num
                current_exp += 1
                
		
            try:
                modulo_list[int_num] += 1
            except:
                modulo_list[int_num] = 1

    return modulo_list

def get_modulo_list():
    modfile = file('modfile','r')
    modulo_list = pickle.load(modfile)
    modfile.close()

def get_coeff_list_actual(n, modulo_list):
    return [[(n*x)%250 for x in xrange(0,modulo_list[n])].count(y) for y in xrange(0,250)]

def get_coeff_list():
    coeff_file = file('coeff','r')
    coeff_list = pickle.load(coeff_file)
    coeff_file.close()
    return coeff_list
    

def mul_list (list_1, list_2):
    final_list = list_1[:]
    for exp_num1, coeff1 in enumerate(list_1):
        for exp_num2, coeff2 in enumerate(list_2):
            final_list[(exp_num1 + exp_num2) % 250] += coeff1 * coeff2

    return final_list

def main():
    coeff_list = get_coeff_list()
    list_1 = coeff_list[0]
    list_2 = coeff_list[1]
    int_list = mul_list(list_1, list_2)
    for num in xrange(2,250):
        list_num = coeff_list[num]
        int_list = mul_list(int_list, list_num)

    print int_list[0]
    return int_list

if __name__ == "__main__":
    il=main()
