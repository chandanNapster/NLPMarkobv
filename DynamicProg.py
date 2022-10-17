import time

class DP:

    def __init__(self):
        self.memo = {}


    def fibo(self, n):
        if n <= 2: return n
        else:
            return self.fibo(n-1) + self.fibo(n-2)

    def memoFib(self, n):
        if n in self.memo: return self.memo[n]
        if n <= 2: return n 
        else: 
            fib = self.memoFib(n-1) + self.memoFib(n-2)
            self.memo[n] = fib
            # print(self.memo)
            return fib 


    def fiboBottomUp(self, n):
        fib = {}
        for k in range(n+1):
            if k <= 2: fib[k] = k
            else: 
                f = fib[k-1] + fib[k-2]
                fib[k] = f 
        return fib[k]



    def timeModule(self):
        return time.time()


if __name__ == '__main__':
    d = DP()
    # print("FIBO")
    # start_time_fibo = d.timeModule()
    # d.fibo(38)
    # end_time_fibo = d.timeModule()
    # total_time_fibo = end_time_fibo -start_time_fibo
    # print(total_time_fibo)
    # print(d.fibo(5))
    # print(d.memoFib(5))
    print("MEMO FIBO")
    start_time_memo = d.timeModule()
    print(d.memoFib(100))
    end_time_memo = d.timeModule()
    total_time_memo = end_time_memo -start_time_memo
    print("Time taken",total_time_memo)

    print(d.fiboBottomUp(100))