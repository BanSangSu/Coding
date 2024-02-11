'''
    https://www.acmicpc.net/problem/1854

    Dijkstra algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq
# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

n, m, k = map(int, read_line().split())
graph = [[] for _ in range(n+1)]

def dijkstra(v):
    distances = [[INF for _ in range(k)] for _ in range(n+1)]
    distances[v][0] = 0
    hq = []
    heapq.heappush(hq, (0, v))

    while hq:
        cur_dist, cur_node = heapq.heappop(hq)
        if distances[cur_node][k-1] < cur_dist:
            continue

        for next_node, next_dist in graph[cur_node]:
            distance = cur_dist + next_dist
            if distance < distances[next_node][k-1]:
                distances[next_node][k-1] = distance
                distances[next_node].sort()
                heapq.heappush(hq, (distance, next_node))
    
    return distances


for _ in range(m):
    a, b, c = map(int, read_line().split())
    graph[a].append((b, c))

distances = dijkstra(1)

for i in range(1, n+1):
    print(-1) if distances[i][k-1] == INF else print(distances[i][k-1])