'''
    https://www.acmicpc.net/problem/2579
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
stairs = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(N):
    stairs[i] = (int(read_line()))
dp[0] = stairs[0]
dp[1] = max(stairs[0] + stairs[1], stairs[1])
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
for i in range(3, N):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N-1])