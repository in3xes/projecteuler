'''To find the largest 3 digit * 3 digit product which is a palindrome.'''

import math

# All even-digit palindromes are multiples of 11.

# Begin with the largest 3 digit multiple of 11

# OR : Get all palindromes
# ABC * DEF = <Some 6-digit number>
# Get all 6-digit palindromes <= 999*999 = 998001
# Start from {997}{799} -> {996}{rev(996)=699} and so on

LAST_NUM = 997

def isInteger(num):
    if num == int(num) and int(num) >= 100 and int(num) < 1000:
        return 1
    
def isProduct(num):
    #print "org num is:", num
    for divisor in range(990, 99, -11):

        div = float(num)/divisor
        #print "divisor is:", divisor, "div is:", div
        if isInteger(div) == 1:
            print "Number is:", num
            print "div is:", div
            print "Divisor is:", divisor
            return 1
        
    
    
def reverse(str_inp):
    return str_inp[::-1]


current_num = LAST_NUM
num = int (str(current_num) + reverse(str(current_num)))

while isProduct(num) != 1:
    current_num = current_num - 1
    num = int (str(current_num) + reverse(str(current_num)))
    






