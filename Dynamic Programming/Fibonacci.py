FiboSol = {}

def Fibo(n):
    
    print(FiboSol)
    if n == 0:
        FiboSol.update({0:0})
        return 0
    elif n == 1:
        FiboSol.update({1:1})
        return 1
    else: 
        return Fibo(n-1) + Fibo(n-2)
        # FiboSol.update({n : f3})
        
    # print(FiboSol)

print(FiboSol)
print(Fibo(6))