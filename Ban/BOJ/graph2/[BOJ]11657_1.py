'''
    https://www.acmicpc.net/problem/11657
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

class Graph():
    
    def __init__(self, vertices, edges) -> None:
        self.V = vertices
        self.E = edges
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))
        
    def bellman_ford(self, src):
        self.distances = [INF for _ in range(self.V+1)]
        self.distances[src] = 0

        for _ in range(self.V-1):
            for u, v, w in self.graph:
                if self.distances[u] != INF and self.distances[u] + w < self.distances[v]:
                    self.distances[v] = self.distances[u] + w
                    
        for u, v, w in self.graph:
            if self.distances[u] != INF and self.distances[u] + w < self.distances[v]:
                return False
        
        return self.distances


if __name__ == '__main__':
    N, M = map(int, read_line().split()) # N = vertices, M = edges
    
    graph = Graph(N, M)
    for _ in range(M):
        graph.add_edge(*map(int, read_line().split()))
        
    distances = graph.bellman_ford(1)
    
    if not distances:
        print(-1)
    else:
        for dist in distances[2:]:
            print(dist if dist != INF else -1)
        