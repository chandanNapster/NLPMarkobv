

def FiboBU(n):
    solist = [0,1]

    for i in range(2,n + 1):
        solist.append(solist[i-1] + solist[i-2])
    
    lenList = len(solist)
    return solist[lenList - 1]    


def FiboBUv2(n):
    current, prev, before_prev = 0,0,0
    prev = 1
    before_prev = 0
    for i in range(2,n + 1):
        current = prev + before_prev
        before_prev = prev
        prev = current
    return current      



print("BOTTOM UP v1",FiboBU(1000))
# print("BOTTOM UP v2",FiboBUv2(998))