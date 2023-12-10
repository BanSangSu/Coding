'''
    https://www.acmicpc.net/problem/11404
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

N = int(read_line()) + 1
M = int(read_line())

graph = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, read_line().split())
    if graph[a][b] > c: graph[a][b] = c


def floyd_warshall():
    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                if i == j:
                    graph[i][j] == 0
                else:
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    
floyd_warshall()

for i in range(1, N):
    for j in range(1, N):
        print(0 if graph[i][j] == INF else graph[i][j], end=" ")
    print()
