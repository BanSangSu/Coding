'''
    https://www.acmicpc.net/problem/3176
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque
from math import ceil, log2, floor

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
roads = [() for _ in range(N+1)]
for _ in range(N-1):
    road_tmp = list(map(int, read_line().split()))

    roads[road_tmp[0]] += ((road_tmp[1], road_tmp[2]), )
    roads[road_tmp[1]] += ((road_tmp[0], road_tmp[2]), )

max_2n = int(ceil(log2(N)))
ancestor = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]
min_distances = [[sys.maxsize for _ in range(max_2n+1)] for _ in range(N+1)]
max_distances = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]

depths = [0 for _ in range(N+1)]
q = deque()

q.append((1, 1, 0))
while q:
    node, parent, dist = q.popleft()
    depths[node] = depths[parent] + 1
    ancestor[node][0] = parent
    min_distances[node][0], max_distances[node][0] = dist, dist

    for j in range(1, max_2n+1):
        ancestor[node][j] = ancestor[ancestor[node][j-1]][j-1]
        min_distances[node][j] = min(min_distances[node][j-1], min_distances[ancestor[node][j-1]][j-1])
        max_distances[node][j] = max(max_distances[node][j-1], max_distances[ancestor[node][j-1]][j-1])
    for child, dist in roads[node]:
        if child != parent:
            q.append((child, node, dist))

def get_lca(a, b):
    depth_diff = depths[a] - depths[b]
    if depth_diff < 0:
        a, b = b, a
        depth_diff *= -1
    t_min = sys.maxsize
    t_max = 0

    while depth_diff != 0:
        i = int(floor(log2(depth_diff)))
        t_min = min(t_min, min_distances[a][i])
        t_max = max(t_max, max_distances[a][i])
        a = ancestor[a][i]
        depth_diff = depths[a] - depths[b]

    k = max_2n-1
    while a != b:
        while ancestor[a][k] == ancestor[b][k] and k > 0:
            k -= 1
        t_min = min(t_min, min_distances[a][k], min_distances[b][k])
        t_max = max(t_max, max_distances[a][k], max_distances[b][k])
        a, b = ancestor[a][k], ancestor[b][k]
    return t_min, t_max

K = int(read_line())
for i in range(K):
    a, b = map(int, read_line().split())
    print(*get_lca(a, b))
