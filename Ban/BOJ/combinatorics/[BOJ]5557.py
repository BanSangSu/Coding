'''
    https://www.acmicpc.net/problem/5557

    Dynamic Programming
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

nums = list(map(int, read_line().split()))

# DP
NUM = 21
dp = [[0 for _ in range(NUM)] for _ in range(N)]

# Initialise first number
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for j in range(NUM):
        # If the row has histories of the past calculations
        if dp[i-1][j]:
            # Addition
            if 0 <= j + nums[i] < NUM:
                dp[i][j + nums[i]] += dp[i-1][j]
            
            # Subtraction
            if 0 <= j - nums[i] < NUM:
                dp[i][j - nums[i]] += dp[i-1][j]

# Print the number of cases where the calculation of numbers matches the last number.
print(dp[-2][nums[-1]])

# # DFS => Timeout
# check = [0] * N

# def dfs(depth, val):
#     cnt = 0
#     if depth == N-1:
#         if val == nums[N-1]:
#             return 1
#         return 0
#     elif val < 0 or 20 < val:
#         return 0
    
#     cnt += dfs(depth+1, val + nums[depth])
#     cnt += dfs(depth+1, val - nums[depth])

#     return cnt

# cnt = dfs(0, 0)
# print(cnt)