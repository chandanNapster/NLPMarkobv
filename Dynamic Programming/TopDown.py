

def FiboTD(n, numlist = None):
    numlist = {} if numlist is None else numlist
    # print("##################")
    # print(numlist)
    if numlist is not {} and n in numlist:
        return numlist[n]
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else: 
        fibo = FiboTD(n-1,numlist) + FiboTD(n-2, numlist)
        numlist[n] = fibo
        return fibo 

        
print("TOP DOWN",FiboTD(999))        

# fiblist = {}        

# def Fibo(n):
#     if n in fiblist:
#         # print("Yes")
#         return fiblist[n]
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         # print("Hello", fiblist)
#         fibo = Fibo(n-1) + Fibo(n-2)
#         fiblist[n] = fibo
#         return fibo          
    


# print(Fibo(998))

# print("$$$$$$$$$$$")
# print(fiblist)