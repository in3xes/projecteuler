## The maximum possible product is:
## 9*9*9*9*9 = 9^5
## Minimum is 0, when any of the digits is 0
## If the numbers are: abcde, where eg. c is zero,
## Then we need to skip to the digit after c, i.e., d.
## Assuming we multiply from left to right.


## Start with the first digit.
## Let the product of the first 5 digits be x.
## Take the initial maximum as 4**5=1024.
## 
input_file = open("num", "r")
NUMBER = ""
for line in input_file:
    NUMBER = NUMBER + line.strip('\n')

#print "The number is: ", int(NUMBER)
input_file.close()

ignored_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
# while ignored_digits != []:
#     while True:
#         p = 0
#         if number has digit in ignored_digit:
#             pass

#         else:
#             save product as p1
#             if p1>p:
#                 p = p1

#         try:
#             move to next number

#         except:
#             if p!=0:
#                 return p
#             else:
#                 remove last digit from ignored_digits
#                 shift pointer to first digit



pointer = 0

def findmaxproduct(num):
    pointer = 0
    p = 0
    while True:

        #print "ignored digits are:", ignored_digits

        num5 = num[pointer:pointer+5]

        #print "num5 is:", num5, "len is:", len(num5)

        
        while len(num5) == 5:

            #print "ignored digits are:", ignored_digits

            

            #print map(lambda elem: elem in ignored_digits, num5)
            #print map(lambda elem: elem, num5)
            if True not in map(lambda elem: elem in ignored_digits, num5):

                #print "Yes!"
                p1 = 1
                for el in num5:
                    p1 = p1 * int(el)

                if p1 > p:
                    p = p1

                #print "p is:", p
                #print "p1 is:", p1

            pointer = pointer + 1
            num5 = num[pointer:pointer + 5]

        if p!=0:
            return p
        
        else:
            ignored_digits.pop()
            pointer = 0
            num5 = num[pointer:pointer+5]


print findmaxproduct(NUMBER)
	            

    
    





