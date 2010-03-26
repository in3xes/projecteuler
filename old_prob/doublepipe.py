import math

def m(f, d = 1000):
    return f*d/3600000.0

def q(m, t_i, t_o, cp = 4186.0):
    return abs(m*cp*(t_i-t_o))

def lmtd(thi, tho, tci, tco, f_t = "Parallel"):
    if f_t == "Parallel":
        return (((thi-tci) - (tho-tco))/math.log((thi-tci)/(tho-tco)))
    else:
        return (((thi-tco) - (tho-tci))/math.log((thi-tco)/(tho-tci)))

def a(d, l):
    return math.pi*d*l

def u(m, t_i, t_o, a, cp = 4200.0):
    return q(m, t_i, t_o, cp)/(a * abs(t_i - t_o))

fc = 150
fh = 200
thi = 59
tho = 54.6
tci = 30
tco = 36.3
ft = 0

ai = 0.047752
ao = 0.063837

def main():
    while 1:
        
        fh = input("Enter Fh:")
        thi = input("Enter Th_i:")
        tho = input("Enter Th_o:")
        
        fc = input("Enter Fc:")
        tci = input("Enter Tc_i:")
        tco = input("Enter Tc_o:")
        ft = input("Enter 0 for parallel or 1 for counterflow:")


        mc = m(fc)
        mh = m(fh)
        qc = q(mc, tci, tco)
        qh = q(mh, thi, tho)
        qa = (qc + qh) / 2.0

        if ft == 1:
            LMTD = lmtd(thi, tho, tci, tco, "Counterflow")
        else:
            LMTD = lmtd(thi, tho, tci, tco)

        ui = qa / (ai * LMTD)
        uo = qa / (ao * LMTD)

        print (" Fc      Fh      Qc      Qh     Qa    LMTD    Ui    Uo")
        print ("%.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f") % (fc, fh, qc, qh, qa, LMTD, ui, uo)


if __name__ == "__main__":
    main()
    
    
