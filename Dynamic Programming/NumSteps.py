num_of_steps = 16

step_type_1 = 1
step_type_2 = 2
step_type_3 = 3

def steps(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return steps(n-1) + steps(n-2) + steps(n-3)


print(steps(5))