


look_up = {}
num = 0

def cal_fibo(n, look_up):
    
    # look_up = list(set(look_up))
    # if n in look_up: return look_up[n]
    lookUp = list(set(look_up)) 
    print(lookUp)

    if num in look_up: return num 
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num = cal_fibo(n-1, look_up) + cal_fibo(n-2, look_up)
        
        # look_up = list(set(look_up))
        return num          


print(cal_fibo(11, look_up))


