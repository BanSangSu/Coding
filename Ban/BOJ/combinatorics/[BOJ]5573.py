'''
    https://www.acmicpc.net/problem/5573

    Dynamic Programming
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

H, W, N = map(int, read_line().split())

DOWN, RIGHT = 0, 1
trails = [ [*map(int, read_line().split())] for _ in range(H)]

# DP
dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[0][0] = N - 1
for i in range(H):
    for j in range(W):
        if trails[i][j] == DOWN:
            dp[i][j+1] += dp[i][j]//2
            dp[i+1][j] += (dp[i][j]+1)//2
        else: # RIGHT
            dp[i][j+1] += (dp[i][j]+1)//2
            dp[i+1][j] += dp[i][j]//2

ans_x, ans_y = 0, 0
while ans_x < H and ans_y < W:
    if (trails[ans_x][ans_y]+dp[ans_x][ans_y]) % 2 == DOWN:
        ans_x += 1
    else:
        ans_y += 1
print(ans_x+1, ans_y+1)


# # Timeout!
# for _ in range(N):
#     i, j = 0, 0
#     while i < H and j < W:
#         now = trails[i][j]

#         if now == DOWN:
#             trails[i][j] = RIGHT
#             i += 1
#         elif now == RIGHT:
#             trails[i][j] = DOWN
#             j += 1

# print(i+1, j+1)
