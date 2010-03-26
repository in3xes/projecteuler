from math import *
    
def Wi(h):
    h=float(h)
    r = 14.5
    return (pi*h*h*(r-(h/3)))

h=1
while True:
    h = raw_input()
    print Wi(h)
    if h=='0':
        break
