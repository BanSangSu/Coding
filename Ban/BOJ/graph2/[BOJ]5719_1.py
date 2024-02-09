'''
    https://www.acmicpc.net/problem/5719

    Dijkstra algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

while True:
    N, M = map(int, read_line().split())
    if N == 0 and M == 0:
        break

    S, D = map(int, read_line().split())

    adj = [[] for _ in range(N)]
    reverse_adj = [[] for _ in range(N)]
    check = [[False for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        U, V, P = map(int, read_line().split())
        adj[U].append((V, P))
        reverse_adj[V].append((U, P))

    dist = [INF for _ in range(N)]
    dijkstra_1(dist, adj, check, S)
    dijkstra_2(dist, reverse_adj, check, S, D)

    dist = [INF for _ in range(N)]
    dijkstra_1(dist, adj, check, S)

    print(dist[D] if dist[D] != INF else -1)