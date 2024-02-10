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
    heapq.heappush(hq, (v, 0))

    while hq:
        cur_node, cur_dist = heapq.heappop(hq)

        if dist[cur_node] < cur_dist:
            continue

        for (next_node, next_dist) in adj[cur_node]:
            distance = cur_dist + next_dist
            if distance < dist[next_node] and check[cur_node][next_node] == False:
                dist[next_node] = distance
                heapq.heappush(hq, (next_node, distance))

def dijkstra_2(dist, reverse_adj, check, s, v):
    hq = []
    heapq.heappush(hq, (v, dist[v]))

    while hq:
        cur_node, cur_dist = heapq.heappop(hq)

        if cur_node == s:
            continue

        for (past_node, past_dist) in reverse_adj[cur_node]:
            if check[past_node][cur_node] == True:
                continue

            if dist[past_node] == dist[cur_node] - past_dist:
                check[past_node][cur_node] = True
                heapq.heappush(hq, (past_node, dist[past_node]))

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