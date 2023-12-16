'''
    https://www.acmicpc.net/problem/11400
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

sys.setrecursionlimit(10**6)

V, E = map(int, read_line().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B = map(int, read_line().split())
    
    graph[A].append(B)
    graph[B].append(A)
    
articulation = []
discover = [0 for _ in range(V+1)]

def dfs(cur, parent, idx):
    discover[cur] = idx
    low = idx
    idx += 1
    
    for next in graph[cur]:
        if next == parent:
            continue
        
        if discover[next]:
            low = min(low, discover[next])
        else:
            child = dfs(next, cur, idx)
            low = min(low, child)
            if discover[cur] < child:
                articulation.append(tuple(sorted((cur, next))))
         
    return low

dfs(1, 0, 1)

articulation.sort()
print(len(articulation))
for edge in articulation:
    print(*edge)