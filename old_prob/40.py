
import number_op

def main():
    counter = 0
    product = 1
    counter_expected = 1
    for i in xrange(1, 500000):
        for digit in str(i):
            counter += 1
            if counter == counter_expected:
                #print counter,",",digit,",",i
                product *= int(digit)
                counter_expected *= 10

            if counter == 1000000:
                return product

print main()
