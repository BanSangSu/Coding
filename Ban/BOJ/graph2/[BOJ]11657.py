'''
    https://www.acmicpc.net/problem/11657

    Bellman-Ford algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

class Graph:

    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def bellman_ford(self, src):
        dist = [INF for _ in range(self.V + 1)]
        dist[src] = 0

        for _ in range(self.V - 1): # To relax all edges(watch a video on Coding 11657 Notion)
            for u, v, w in self.graph:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                # Graph contains negative weight cycle
                return False

        return dist

if __name__ == '__main__':
    N, M = map(int, read_line().split()) # N = vertices, M = edges
    
    g = Graph(N)
    for _ in range(M):
        A, B, C = map(int, read_line().split())
        g.add_edge(A, B, C)

    dist = g.bellman_ford(1)

    if not dist:
        print(-1)
    else:
        for d in dist[2:]:
           print(d if d != INF else -1)