'''
    https://www.acmicpc.net/problem/1922

    Kruskal Algorithm(Use Union-Find)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(read_line())
M = int(read_line())

parent = [i for i in range(N+1)]
graph = []
answer = 0
for i in range(M):
    a, b, c = map(int, read_line().split())
    graph.append((c, a, b))

graph.sort(key=lambda x: x[0])
for cost, a, b in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
print(answer)
