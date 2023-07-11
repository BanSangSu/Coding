'''
    https://www.acmicpc.net/problem/1516

    Topological Sort
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque 

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

cost = [0 for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]

graph = defaultdict(list)
for i in range(1, N+1):
    tmp = list(map(int, read_line().split()))[:-1]
    cost[i] = tmp[0]
    for e in tmp[1:]:
        graph[e].append(i)
        in_degree[i] += 1

def topology_sort():
    answer = [0 for _ in range(N+1)]
    queue = deque()
    
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            answer[i] = cost[i]

    while queue:
        now = queue.popleft()
        for e in graph[now]:
            in_degree[e] -= 1
            
            answer[e] = max(answer[e], cost[e] + answer[now])

            if in_degree[e] == 0:
                queue.append(e)

    print(*answer[1:], sep='\n')

topology_sort()