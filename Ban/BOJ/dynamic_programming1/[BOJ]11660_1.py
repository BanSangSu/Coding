'''
    https://www.acmicpc.net/problem/11660
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())

grid = [[*map(int, read_line().split())] for _ in range(N)]
grid_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        grid_sum[i][j] = grid_sum[i-1][j] + grid_sum[i][j-1] - grid_sum[i-1][j-1] + grid[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read_line().split())
    print(grid_sum[x2][y2] - grid_sum[x2][y1-1] - grid_sum[x1-1][y2] + grid_sum[x1-1][y1-1])