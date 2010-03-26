import math

def digits(num):
    '''Gets individual digits, starting from the units place.
    (Generator)'''
    if num == 0:
        yield 0
        
    while num > 0:
        yield num % 10
        num /= 10

def convert_to_base(dec_num, base = 2):
    place_number = 1
    binary_num = 0

    while 1:
        quotient = dec_num // base
        modulus = dec_num % base
        binary_num += modulus * place_number
        place_number *= 10
        dec_num = quotient
        if quotient < 1:
            break
    return binary_num

def convert_to_binary(dec_num):
    return convert_to_base(dec_num, base=2)

def convert_to_decimal(num, base = 2):
    dec_num = 0
    place_number = 0
    
    while num >= 1:
        digit = num % 10
        dec_num += digit * (base ** place_number)
        num /= 10
        place_number += 1

    return dec_num

def get_reverse(num):
    '''Gets the reverse of a positive number.'''
    
    try:
        max_ten_power = int(math.log10(num))
    except ValueError:                  # log not defined
        return 0
    
    place_number = max_ten_power
    rev_num = 0
    
    for digit in digits(num):
        place_value = 10**place_number    
        rev_num += place_value * digit
        place_number -= 1

    return rev_num

    
