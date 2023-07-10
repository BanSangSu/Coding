'''
    https://www.acmicpc.net/problem/2458

    Floyd-Warshall Algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

# Pypy pass
N, M = map(int, read_line().split())
heights = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    small, tall = map(int, read_line().split())
    heights[small][tall] = 1

# Floyd-Warshall
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if heights[i][j] == 1 or (heights[i][k] == 1 and heights[k][j] == 1):
                heights[i][j] = 1

# Print answer
answer = 0
for i in range(1, N+1):
    check = 0
    for j in range(1, N+1):
        check += (heights[i][j] + heights[j][i])
    if check == N-1: # When you know the order of heights
        answer += 1
print(answer)
