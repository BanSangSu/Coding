'''
    https://www.acmicpc.net/problem/11051
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

import math
# sys.stdin = open("data.txt", 'r')

N, K = map(int, read_line().split())

result = math.comb(N, K)
print(result%10007)

# dp = [[1 for _ in range(i+1)] for i in range(N+1)]

# for i in range(2, N+1):
#     for j in range(1, i):
#         dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
# print(dp[N][K]%10007)