
# The n^(th) term of the sequence of triangle numbers is given by,
# t_(n) = 0.5*n(n+1); so the first ten triangle numbers are:

#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#     By converting each letter in a word to a number corresponding to
#     its alphabetical position and adding these values we form a word
#     value. For example, the word value for SKY is 19 + 11 + 25 = 55
#     = t_(10). If the word value is a triangle number then we shall
#     call the word a triangle word.

#     Using words.txt (right click and 'Save Link/Target As...'), a
#     16K text file containing nearly two-thousand common English
#     words, how many are triangle words?
    
import char_op
import csv
import math

def get_term(n):
    '''nth term of triangle numbers.'''

    val = (n*(n+1)/2)
    print val
    return val

def check_triangle(num):
    '''Checks if triangle number or not.'''

    val = math.sqrt(8*num + 1)/2
    val_pos = val - 0.5
    if val_pos == int(val_pos):
        return True
    return False

def main():
    f_inp = open("words.txt", 'r')
    csv_reader = csv.reader(f_inp)
    #print csv_reader
    #print dir(csv_reader)
    counter = 0
    for word in csv_reader.next():
        word_val = char_op.string_val(word)
        if check_triangle(word_val):
            counter += 1
            #print word

    print "There are", counter, "triangle words."
    f_inp.close()
        
if __name__ == "__main__":
    main()
