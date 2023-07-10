'''
    https://www.acmicpc.net/problem/11438

    Lowest Common Ancestor(LCA)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

# sys.stdin = open("data.txt", 'r')

# Pypy can pass!
LOG = 22 # 2^21

N = int(read_line())
parent = [[0] * LOG for _ in range(N+1)]
visited = [False for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, read_line().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, d):
    visited[x] = True
    depth[x] = d

    for node in graph[x]:
        if visited[node]:
            continue
        parent[node][0] = x
        dfs(node, d + 1)

def set_parent():
    dfs(1, 0) # Update only parent information directly above.
    for i in range(1, LOG): # Update all parent information using above information.
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    # b is always deeper than a
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(LOG-1, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a # lca complete
    
    # Find common ancester as you go up(from leaf node)
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]


set_parent()

M = int(read_line())
for _ in range(M):
    a, b = map(int, read_line().split())
    print(lca(a, b))

