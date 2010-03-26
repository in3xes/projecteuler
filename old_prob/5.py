# To find the smallest number divisible by each of the numbers 1 to 20
# PRO=1
# LI=range(2,21)
# Start from 2
# Divide each element by the number till no more elements are divisible
# PRO=PRO * the number for each time the above is done


LAST_NUM=20
LI=range(2,LAST_NUM + 1)

listnum = LI[:]

PRO=1
def divideList (num):
    global listnum
    listtemp = listnum[:]
    listnum = map(lambda x: x%num == 0 and x/num or x, listnum)
    if listnum == listtemp:
        return 0
    else:
        return 1

for num in range(2,LAST_NUM + 1):
    while 1==1:
        if divideList(num) == 1:
            
            PRO = PRO * num
            print "PRO is:", PRO, " num is ", num
            print "listnum is:", listnum
        
        else:
            break
print "PRO is:", PRO


    

    

