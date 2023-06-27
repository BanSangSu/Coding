'''
    https://www.acmicpc.net/problem/11051

    Dynamic Programming
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, K = map(int, read_line().split())

# DP version
dp = [[1 for _ in range(N+1)] for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[N][K]%10007)


# # Easy version
# import math
# r = math.comb(N,K)
# print(r%10007)

# # Recursion Error
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

# n_factorial = factorial(N)
# k_factorial = factorial(K)
# n_minus_k_factorial = factorial(N-K)
# print((n_factorial//(k_factorial*n_minus_k_factorial))%10007)