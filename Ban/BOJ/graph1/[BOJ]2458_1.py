'''
    https://www.acmicpc.net/problem/2458
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())
# Dictonary for identifying who is bigger or smaller than themselves.
height_dict = defaultdict(set)
answer = 0

def dfs(start, current_node, visited):
    visited[current_node] = True
    for next_node in graph[current_node]:
        if not visited[next_node]:
            height_dict[start].add(next_node)
            height_dict[next_node].add(start)
            dfs(start, next_node, visited)

# Edge graph which points a(small) to b(big).
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, read_line().split())
    graph[a].append(b)

# DFS which start point is itself
# All nodes are taller than start point. 
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i,i, visited)

# [students who is bigger than itself + students who is smaller than itself] is N-1.  
for i in range(1, N+1):
    if len(height_dict[i]) == N-1:
        answer += 1
print(answer)
