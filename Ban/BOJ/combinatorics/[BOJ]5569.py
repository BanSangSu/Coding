'''
    https://www.acmicpc.net/problem/5569

    Dynamic Programming
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

W, H = map(int, read_line().split())

# x and y are on coordinate system.
# [x][y][Is_the direction from East(0) or North(1)?][can_change_direction(1) or not(0)]
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(H+1)] for _ in range(W+1)]

# 0 is East, 1 is North.
# 0 is impossible, 1 is possible.
# Initialise edges of the coordinate system
for i in range(2, W+1):
    dp[i][1][0][1] = 1
for i in range(2, H+1):
    dp[1][i][1][1] = 1

for x in range(2, W+1):
    for y in range(2, H+1):
        dp[x][y][0][0] = dp[x-1][y][1][1]
        dp[x][y][0][1] = dp[x-1][y][0][0] + dp[x-1][y][0][1]
        dp[x][y][1][0] = dp[x][y-1][0][1]
        dp[x][y][1][1] = dp[x][y-1][1][0] + dp[x][y-1][1][1]
result = sum(dp[W][H][0]) + sum(dp[W][H][1])
print(result % 100000)