'''
    https://www.acmicpc.net/problem/11660
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, read_line().split())))

matrix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        matrix_sum[i][j] = matrix_sum[i][j-1] + matrix_sum[i-1][j] - matrix_sum[i-1][j-1] + matrix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read_line().split())
    print(matrix_sum[x2][y2] - matrix_sum[x2][y1-1] - matrix_sum[x1-1][y2] + matrix_sum[x1-1][y1-1])
