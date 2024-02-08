'''
    https://www.acmicpc.net/problem/3860

   Shortest Path Faster Algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import collections

from typing import Mapping, Optional, Sequence

# sys.stdin = open("data.txt", 'r')

WGraph = Sequence[Mapping[int, float]]

INF = float("inf")

def spfa(wgraph:WGraph, source: int, prev: Optional[list[int]] = None) -> list[float]:
    size = len(wgraph)
    lengths = [0] * size
    is_in_queue = [False] * size
    is_in_queue[source] = True
    distances = [INF] * size
    distances[source] = 0
    if prev:
        prev[source] = None
    
    queue = collections.deque([source])
    while queue:
        u = queue.popleft()
        is_in_queue[u] = False
        length_u, dist_u = lengths[u], distances[u]
        if length_u == size:
            dist_u = distances[u] = -INF
        for v, dist_uv in wgraph[u].items():
            dist_v = dist_u + dist_uv
            if distances[v] <= dist_v:
                continue
            distances[v], lengths[v] = dist_v, length_u + 1
            if prev:
                prev[v] = u
            if not is_in_queue[v]:
                queue.append(v)
                is_in_queue[v] = True

    return distances


def main():
    while True:
        W, H = [int(x) for x in read_line().split()]
        if W == H == 0:
            break

        G = int(read_line())
        graves = set()
        for _ in range(G):
            X, Y = [int(x) for x in read_line().split()]
            graves.add(Y * W + X)

        wgraph = [{} for _ in range(W * H)]
        E = int(read_line())
        for _ in range(E):
            X1, Y1, X2, Y2, T = [int(x) for x in read_line().split()]
            source, dest = Y1 * W + X1, Y2 * W + X2
            wgraph[source][dest] = T

        for source, edges in enumerate(wgraph):
            if wgraph[source]:
                continue
            y, x = divmod(source, W)
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                dest = ny * W + nx
                if 0 <= nx < W and 0 <= ny < H and dest not in graves:
                    edges[dest] = 1
        wgraph[W * H - 1].clear()

        dists = spfa(wgraph, 0)
        if -INF in dists:
            print("Never")
        else:
            dist_to_dset = dists[W * H - 1]
            print("Impossible" if dist_to_dset == INF else dist_to_dset)


if __name__=="__main__":
    main()