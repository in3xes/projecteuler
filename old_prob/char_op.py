alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabets_dict():
    global alphabets
    alphabets_dict = {}
    for num, letter in enumerate(alphabets):
        alphabets_dict[letter] = num + 1

    return alphabets_dict
alphabets_dict = alphabets_dict()

def string_val(str_inp):
    global alphabets_dict
    val = 0
    for character in str_inp:
        try:
            val += alphabets_dict[character]
        except KeyError:
            continue
    return val




    
