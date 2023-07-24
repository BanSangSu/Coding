'''
    https://www.acmicpc.net/problem/5719

    Dijkstra algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize
def dijkstra_1(dist, adj, check, v):
    dist[v] = 0
    hq = []
    heapq.heappush(hq, (0, v))

    while hq:
        cur_dist, cur = heapq.heappop(hq)

        if dist[cur] < cur_dist:
            continue

        for (next, next_dist) in adj[cur]:
            distance = cur_dist + next_dist
            if distance < dist[next] and check[cur][next] == False:
                dist[next] = distance
                heapq.heappush(hq, (distance, next))

def dijkstra_2(dist, reverse_ajd, check, s, v):
    hq = []
    heapq.heappush(hq, (dist[v], v))

    while hq:
        cur_dist, cur = heapq.heappop(hq)

        if cur == s:
            continue
        for (past, past_dist) in reverse_ajd[cur]:
            if check[past][cur] == True:
                continue

            if dist[past] == dist[cur] - past_dist:
                check[past][cur] = True
                heapq.heappush(hq, (dist[past], past))

while True:
    N, M = map(int, read_line().split())

    if N == 0 and M == 0:
        break

    S, D = map(int, read_line().split())
        
    adj = [[] for _ in range(N)]
    reverse_ajd = [[] for _ in range(N)]
    check = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, read_line().split())
        adj[U].append((V, P))
        reverse_ajd[V].append((U, P))

    dist = [INF for _ in range(N)]
    dijkstra_1(dist, adj, check, S)
    dijkstra_2(dist, reverse_ajd, check, S, D)

    dist = [INF for _ in range(N)]
    dijkstra_1(dist, adj, check, S)

    print(dist[D] if dist[D] != INF else -1)
    