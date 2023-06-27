'''
    https://www.acmicpc.net/problem/1010

    Dynamic Programming
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

T = int(read_line())

# DP version 2
def bridge2(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:    
                dp[i][j] = j
            else:
                if i == j:
                    dp[i][j] = 1
                elif i < j:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    return dp[n][m]

# # DP version 1
# def bridge1(n, m):
#     dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

#     for i in range(1, m+1):
#         dp[1][i] = i

#     for j in range(2, n+1):
#         for k in range(j, m+1):
#             for l in range(k, j-1, -1):
#                 dp[j][k] += dp[j-1][l-1]

#     return dp[n][m]

for _ in range(T):
    N, M = map(int, read_line().split())
    
    # # Simple version(Combination)
    # result = math.comb(M, N)
    # print(result)

    print(bridge2(N, M))

