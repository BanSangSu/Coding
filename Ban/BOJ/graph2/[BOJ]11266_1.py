'''
    https://www.acmicpc.net/problem/11266
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

# sys.stdin = open("data.txt", 'r')

def dfs(V, E, graph):
    D = [0] * V # discovery time
    low = [0] * V # lowest reachable vertex
    parent = [-1] * V
    child = [0] * V
    articulation_point = [False] * V
    
    cnt = 1
    stack = [*range(V)]
    while stack:
        vertex = stack.pop()
        if vertex < 0: # leaf node of DFS subtree
            vertex = ~vertex # original vertex number
            u = parent[vertex]
            if u != -1: # Not root node
                child[u] += 1
                if low[vertex] >= D[u]: # if u is the parent of v, and v's childs are visited later than u, it is an articulation point.
                    articulation_point[u] = True
                low[u] = min(low[u], low[vertex])
            elif u == -1 and child[vertex] == 1: # if it is a root node and has only one child, it is not an articulation point.
                articulation_point[vertex] = False
                
        if D[vertex]: continue # visited node
        
        D[vertex] = cnt
        low[vertex] = cnt
        cnt += 1
    
        stack.append(~vertex)
        for w in graph[vertex]:
            if not D[w]:
                parent[w] = vertex
                stack.append(w)
            elif w != parent[vertex]:
                low[vertex] = min(low[vertex], D[w])
                
    result = []
    for i, v in enumerate(articulation_point):
        if v: result.append(i + 1)
    
    return result                


def main():
    V, E = map(int, read_line().split())
    graph = defaultdict(list)
    for _ in range(E):
        u,v = map(int,read_line().split())
        u,v = u-1, v-1
        graph[u].append(v)
        graph[v].append(u)
    
    result = dfs(V, E, graph)
    print(f"{len(result)}\n{' '.join(map(str, result))}")
    

if __name__ == "__main__":
    main()
    