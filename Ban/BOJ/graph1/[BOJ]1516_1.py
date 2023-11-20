'''
    https://www.acmicpc.net/problem/1516
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

## Method 2 / Memory: 32140KB, Time: 60ms
N = int(read_line())
T, G = [-1] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    T[i], *G[i], _ = map(int, read_line().split())
t = [-1] * (N + 1)

def get(i):
    if t[i] == -1:
        t[i] = (max(get(n) for n in G[i]) if G[i] else 0) + T[i]
    return t[i]
    
    
print("\n".join(str(get(i)) for i in range(1, N + 1)))

## Method 1 / Memory: 34088KB, Time: 84ms
# class Solution():
#     def __init__(self) -> None:
#         self._calc_build_cost(int(read_line()))

#     def _init_graph(self, N):
#         graph = [[] for _ in range(N)]
#         indgr = [0] * N
#         cost = [0] * N
#         for nn in range(N):
#             c, *pn, _ = map(int, read_line().split())
#             cost[nn] = c
#             indgr[nn] += len(pn)
#             for ppn in map(lambda x: x-1, pn):
#                 graph[ppn].append(nn)
#         return graph, indgr, cost
    

#     def _calc_build_cost(self, N):
#         graph, indgr, cost = self._init_graph(N)
#         build_times = [0] * N
#         cands = [[0] for _ in range(N)]
#         stack = [i for i in range(N) if not indgr[i]]
#         while stack:
#             pn = stack.pop()
#             build_times[pn] = cost[pn] + max(cands[pn])
#             for cn in graph[pn]:
#                 cands[cn].append(build_times[pn])
#                 indgr[cn] -= 1
#                 if not indgr[cn]:
#                     stack.append(cn)
#         self.build_times = build_times

# if __name__ == "__main__":
#     solution = Solution()
#     print("\n".join(map(str, solution.build_times)))
