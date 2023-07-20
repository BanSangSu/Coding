'''
    https://www.acmicpc.net/problem/11404
    
    Floyd-Warshall algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

N = int(read_line())
M = int(read_line())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, read_line().split())
    graph[a][b] = min(graph[a][b], c)


def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

floyd_warshall()
for i in range(1, N+1):
    for j in range(1, N+1):
        print(0 if graph[i][j] == INF else graph[i][j], end=" ")
    print()