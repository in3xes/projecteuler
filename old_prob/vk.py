import pylab
import math
import itertools

R = 8.314

def ctop(c, T):
    # p = cRT
    global R
    return c*R*T

def ptoc(p, T):
    # c = RT/p
    global R
    return R*T/p

# -r = -dc/dt = kc^n

def plot_rate (c, t, order = 1, c0 = None, cb = None, cb0 = None):
    c = map(float, c)
    if c0 is None:
        c0 = c[0]

    if order == 1:
        y_val = map(lambda ca: math.log(c0/ca), c)

    elif order == 2:
        ca = c[:]
        ca0 = c0 or ca[0]
        try:
            cb0 = cb0 or cb[0]
        except:
            pass
        y_val = []
        try:
            for ca_i, ca_b in zip(ca, cb):
                y_val.append(math.log(cb/ca))
        except:
            y_val = map(lambda x: 1/x, ca)
            
        
    print y_val
    pylab.plot(t, y_val, 'o-')
    pylab.title('Order:' + str(order))
    pylab.show()


c1 = [10, 8, 6, 5, 3, 2, 1]
t1 = [0, 20, 40, 60, 120, 180, 300]

p = map(lambda x: x*101325.0/760.0, [760, 600, 475, 390, 320, 275, 240, 215, 150])
c = [ptoc(x, 273) for x in p]
t = [0, 2, 4, 6, 8, 10, 12, 14, 100]

plot_rate(c, t, order = 2)
