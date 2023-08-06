'''
    https://www.acmicpc.net/problem/5626
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
h = list(map(int, read_line().split()))

# Problem that I don't understand how to solve!
# Passed code in Pypy
dp = [[0 for _ in range(min(i+1, N-i))] for i in range(N)]
mod = 10**9 + 7
if h[0] <= 0:
    dp[0][0] = 1
for i in range(1, N):
    for j in range(len(dp[i])):
        for k in range(-1, 2, 1):
            if 0 <= j + k < len(dp[i-1]):
                dp[i][j] = (dp[i][j] + dp[i-1][j + k]) % mod
    if h[i] != -1:
        for l in range(len(dp[i])):
            if l != h[i]:
                dp[i][l] = 0
print(dp[-1][0])