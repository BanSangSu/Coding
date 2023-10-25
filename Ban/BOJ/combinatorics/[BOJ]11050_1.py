'''
    https://www.acmicpc.net/problem/11050
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

import math

# sys.stdin = open("data.txt", 'r')

# def factorial(n):
#     ret = 1
#     for i in range(1, n+1):
#         ret *= i

#     return ret

N, K = map(int, read_line().split())

result = math.factorial(N) // (math.factorial(N-K) * math.factorial(K))
print(result)
