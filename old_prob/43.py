
# The number, 1406357289, is a 0 to 9 pandigital number because it is
# made up of each of the digits 0 to 9 in some order, but it also has
# a rather interesting sub-string divisibility property.

# Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so
# on. In this way, we note the following:

#             d_(2)d_(3)d_(4)=406 is divisible by 2
#             d_(3)d_(4)d_(5)=063 is divisible by 3
#             d_(4)d_(5)d_(6)=635 is divisible by 5
#             d_(5)d_(6)d_(7)=357 is divisible by 7
#             d_(6)d_(7)d_(8)=572 is divisible by 11
#             d_(7)d_(8)d_(9)=728 is divisible by 13
#             d_(8)d_(9)d_(10)=289 is divisible by 17

#                                 Find the sum of all 0 to 9
#                                 pandigital numbers with this
#                                 property.

# d4 has to be a multiple of 2 (0, 2, 4, 6, 8)
# d3+d4+d5 has to be a multiple of 3 (6, 9, 12, 15, 18, 21, 24)
# d6 has to be a multiple of 5 (0, 5)
# d6 - d8 + d7 has to be a multiple of 11
# 

def uniq_num_threedigit(num):
    multiples_list = []
    i = 1
    while 1:
        i += 1
        val = i*num
        if val > 999:
            break
        strp = str(val)
        len_strp = len(strp)
        if len_strp == len(set(strp)):
            if len_strp == 1:
                strp_1 = '00' + strp
                strp = strp_1
            elif len_strp == 2:
                strp_2 = '0' + strp
                strp = strp_2
            #print strp,
            multiples_list.append(strp)
    return multiples_list


unt = uniq_num_threedigit

u17 = unt(17)
u13 = unt(13)
u11 = unt(11)
u7 = unt(7)
u5 = unt(5)
u3 = unt(3)
u2 = unt(2)
u1 = unt(1)
counter = 0

def check_combinations(ua, ub):
    '''Checks for valid combinations of 3 digits
    for two given divisors, adjacent in the number.'''
    
    clist = []
    for ma in ua:
        for mb in ub:
            if ma[1:] != mb[0:2]:
                continue
            conc = ma[0:2] + mb[1:]

            if len(conc) == len(set(conc)):
                clist.append(conc)

    return clist

u1317 = check_combinations(u13,u17)
u111317 = check_combinations(u11, u1317)
u7111317 = check_combinations(u7, u111317)
u57111317 = check_combinations(u5, u7111317)
u357111317 = check_combinations(u3, u57111317)
u2357111317 = check_combinations(u2, u357111317)
u12357111317 = check_combinations(u1, u2357111317)
u_final = u12357111317
u_final = u2357111317
print u_final
print "Sum", sum(map(int, u_final))

