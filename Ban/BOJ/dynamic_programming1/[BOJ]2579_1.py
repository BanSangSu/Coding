'''
    https://www.acmicpc.net/problem/2579
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

stair = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(N) :
    stair[i] = int(read_line())

dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
print(dp[N-1])