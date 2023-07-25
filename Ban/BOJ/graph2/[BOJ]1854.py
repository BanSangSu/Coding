'''
    https://www.acmicpc.net/problem/1854

    Dijkstra algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq
# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

n, m, k = map(int, read_line().split())
graph = [[] for _ in range(n+1) for _ in range(n+1)]

def dijkstra(v):
    dist = [[INF for _ in range(k)] for _ in range(n+1)]
    dist[v][0] = 0
    hq = []
    heapq.heappush(hq, (0, v))

    while hq:
        cur_dist, cur = heapq.heappop(hq)
        if dist[cur][k-1] < cur_dist:
            continue

        for next, next_dist in graph[cur]:
            distance = cur_dist + next_dist
            if distance < dist[next][k-1]:
                dist[next][k-1] = distance
                dist[next].sort()
                heapq.heappush(hq, (distance, next))
    return dist

for _ in range(m):
    a, b, c = map(int, read_line().split())
    graph[a].append((b, c))

dist = dijkstra(1)

for i in range(1, n+1):
    print(-1) if dist[i][k-1] == INF else print(dist[i][k-1])