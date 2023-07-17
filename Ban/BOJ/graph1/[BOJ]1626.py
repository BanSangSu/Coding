'''
    https://www.acmicpc.net/problem/1626

    Mimimum Spanning Tree(MST)
        - Kruskal Algorithm

    Lowest Common Ancestor(LCA)
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()
from math import log2
from collections import deque

# sys.stdin = open("data.txt", 'r')

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    parent_a = find(a, parent)
    parent_b = find(b, parent)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

def bfs(graph, depth, two_weight, parent):
    depth[0] = 0
    q = deque([0])

    while q:
        node = q.popleft()

        for next_node, cost in graph[node]:
            if depth[next_node] != -1:
                continue
                
            depth[next_node] = depth[node] + 1
            parent[next_node][0] = node
            two_weight[next_node][0] = [cost, -1]
            q.append(next_node)

def longest(arr1, arr2):
    temp = list(set(arr1 + arr2))
    temp.sort(reverse=True)

    while len(temp) < 2:
        temp.append(-1)

    temp = temp[:2]
    return temp

def set_parent(graph, depth, two_weight, parent, v, k):
    bfs(graph, depth, two_weight, parent)

    for log in range(1, k):
        for node in range(1, v):
            next_node = parent[node][log-1]
            parent[node][log] = parent[next_node][log-1]
            
            weight1, weight2 = two_weight[node][log-1], two_weight[next_node][log-1]
            two_weight[node][log] = longest(weight1, weight2)

def lca(a, b, depth, two_weight, parent, k):
    ret = [-1, -1]
    if depth[a] > depth[b]:
        a, b = b, a

    for log in range(k-1, -1, -1):
        if depth[b] - depth[a] >= (1 << log):
            ret = longest(ret, two_weight[b][log])
            b = parent[b][log]

    if a == b:
        return ret
    
    for log in range(k-1, -1, -1):
        if parent[b][log] != parent[a][log]:
            ret = longest(ret, two_weight[a][log])
            ret = longest(ret, two_weight[b][log])
            b = parent[b][log]
            a = parent[a][log]

    ret = longest(ret, two_weight[a][0])
    ret = longest(ret, two_weight[b][0])

    return ret

def main():
    v, e = map(int, read_line().split())
    edge, graph, used = [], [[] for i in range(v)], [0 for _ in range(e)]
    parent = [i for i in range(v)]

    for i in range(e):
        a, b, c = map(int, read_line().split())
        a -= 1
        b -= 1
        edge.append((c, a, b))

    edge.sort()
    mst, cnt = 0, 0

    for i in range(e):
        c, a, b = edge[i]

        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            graph[a].append((b, c))
            graph[b].append((a, c))

            used[i] = 1
            mst += c
            cnt += 1

    if cnt != v - 1:
        print(-1)
        return
    
    ans, k = sys.maxsize, int(log2(v)) + 1
    depth, two_weight = [-1 for _ in range(v)], [[[-1, -1] for _ in range(k)] for _ in range(v)]
    parent = [[-1 for _ in range(k)] for _ in range(v)]

    set_parent(graph, depth, two_weight, parent, v, k)
    for i in range(e):
        if used[i]:
            continue

        w, u, v = edge[i]
        weight = lca(u, v, depth, two_weight, parent, k)

        if weight[0] != w:
            ans = min(ans, mst - weight[0] + w)
        elif weight[1] != w and weight[1] != -1:
            ans = min(ans, mst - weight[1] + w)

    if ans == sys.maxsize:
        print(-1)
        return
    
    print(ans)

if __name__ == "__main__":
    main()
    