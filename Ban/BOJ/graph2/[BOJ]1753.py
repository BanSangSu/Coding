'''
    https://www.acmicpc.net/problem/1753

    Dijkstra algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize
V, E = map(int, read_line().split())
start = int(read_line())

def dijkstra(graph, start):
    distances = [INF for _ in range(V+1)]
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (distances[start], start))
    while heap:
        dist, node = heapq.heappop(heap)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(heap, (distance, next_node))

    return distances


graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, read_line().split())
    graph[u].append((v, w))

result_distnaces = dijkstra(graph, start)
for i in range(1, V+1):
    print("INF" if result_distnaces[i] == INF else result_distnaces[i])