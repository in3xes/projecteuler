for i in range(0,17):
    bob = ""
    for k in range(0,i+1):
        if i-k > 9:
            bob += str(k) + "(" + str(i-k) +") "
        elif k > 9:
            bob += "(" + str(k) + ")" + str(i-k) + " "
        else:
            bob += str(k) + str(i-k) + " " 
    bob += "\n"
    print(bob)
