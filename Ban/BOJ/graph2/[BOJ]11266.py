'''
    https://www.acmicpc.net/problem/11266
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
from collections import defaultdict

# sys.stdin = open("data.txt", 'r')

def dfs(graph, order, cutVertex, here, cnt):
    order[here] = cnt

    children = 0
    ret = order[here]

    for next in graph[here]:
        if order[next]:
            ret = min(ret, order[next])

        else:
            children += 1
            subtree = dfs(graph, order, cutVertex, next, cnt + 1)

            if cnt != 1 and subtree >= order[here]:
                cutVertex.add(here)

            ret = min(subtree, ret)
    if cnt == 1 and children >= 2:
        cutVertex.add(here)

    return ret

V, E = map(int, read_line().split())
graph = defaultdict(list)
cutVertex = set()
candidates = set()

for i in range(E):
    A, B = map(int, read_line().split())
    graph[A].append(B)
    graph[B].append(A)
    candidates.add(A)
    candidates.add(B)

order = [None for _ in range(V+1)]
cnt = 1

for vertex in candidates:
    if not order[vertex]:
        dfs(graph, order, cutVertex, vertex, 1)

print(len(cutVertex))

for vertex in sorted(list(cutVertex)):
    print(vertex, end=" ")

