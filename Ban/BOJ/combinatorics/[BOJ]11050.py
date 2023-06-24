'''
    https://www.acmicpc.net/problem/11050
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def factorial(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

N, K = map(int, read_line().split())

n_factorial = factorial(N)
k_factorial = factorial(K)
n_minus_k_factorial = factorial(N-K)

result = n_factorial//(k_factorial*n_minus_k_factorial)
print(result)
