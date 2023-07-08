'''
    https://www.acmicpc.net/problem/2252

    Topological Sort
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())

graph = defaultdict(list)
in_degree = [0 for _ in range(N+1)]
queue = deque()
answer = []

for i in range(M):
    a, b = map(int, read_line().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)

print(*answer)