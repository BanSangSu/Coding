'''
    https://www.acmicpc.net/problem/5573
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

H, W, N = map(int, read_line().split())

DOWN, RIGHT = 0, 1
trails = [[*map(int, read_line().split())] for _ in range(H)]

dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[0][0] = N-1
for i in range(H):
    for j in range(W):
        if trails[i][j] == DOWN:
            dp[i][j+1] += dp[i][j]//2
            dp[i+1][j] += (dp[i][j]+1)//2
        else:
            dp[i][j+1] += (dp[i][j]+1)//2
            dp[i+1][j] += dp[i][j]//2

ans_i, ans_j = 0, 0
while ans_i < H and ans_j < W:
    if (trails[ans_i][ans_j] + dp[ans_i][ans_j]) % 2 == DOWN:
        ans_i += 1
    else:
        ans_j += 1
print(ans_i+1, ans_j+1)