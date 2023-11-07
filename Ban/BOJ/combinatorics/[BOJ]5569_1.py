'''
    https://www.acmicpc.net/problem/5569
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

W, H = map(int, read_line().split())

dp = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]
dp[0][0] = [0,0,1,1]

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        
        dp[i][j][0] =  dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] =  dp[i-1][j][1] + dp[i-1][j][3]
        dp[i][j][2] =  dp[i][j-1][1]
        dp[i][j][3] =  dp[i-1][j][0]

print(sum(dp[H-1][W-1]) % 100000)