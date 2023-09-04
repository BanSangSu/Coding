'''
    https://www.acmicpc.net/problem/2748

'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

sys.stdin = open("data.txt", 'r')

def fibo(n):
    fibo_dp = [1 for _ in range(n)]
    i = 3
    while i < n:
        fibo_dp[i] = fibo_dp[i-1] + fibo_dp[i-2]

        i += 1
    
    print(fibo_dp[-1])



N = int(read_line())
fibo(N+1)