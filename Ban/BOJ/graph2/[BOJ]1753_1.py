'''
    https://www.acmicpc.net/problem/1753
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

def dijkstra(start, graph, V, E):
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

def main():
    V, E = map(int, read_line().split())
    start = int(read_line())
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v , w = map(int, read_line().split())
        graph[u].append((v, w))
        
    result_distances = dijkstra(start, graph, V, E)
    for i in range(1, V+1):
        print("INF" if result_distances[i] == INF else result_distances[i])

if __name__ == "__main__":
    main()