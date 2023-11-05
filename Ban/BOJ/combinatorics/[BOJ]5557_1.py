'''
    https://www.acmicpc.net/problem/5557
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

nums = list(map(int, read_line().split()))

R = 21
dp = [[0 for _ in range(R)] for i in range(N)]
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for j in range(R):
        if dp[i-1][j]:
            if j + nums[i] < R:
                dp[i][j+nums[i]] += dp[i-1][j]
            if j - nums[i] >= 0:
                dp[i][j-nums[i]] += dp[i-1][j]

print(dp[N-2][nums[-1]])
