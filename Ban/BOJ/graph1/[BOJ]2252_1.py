'''
    https://www.acmicpc.net/problem/2252
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque

# sys.stdin = open("data.txt", 'r')

def topology_sort(graph, check, graph_len):
    result = []
    queue = deque()
    
    for i in range(1, graph_len):
        if not check[i]:
            queue.append(i)
    
    while queue:
        tmp = queue.popleft()
        result.append(tmp)
        for i in graph[tmp]:
            check[i] -= 1
            if not check[i]:
                queue.append(i)
    
    return result


def main():
    N, M = map(int, read_line().split())
    graph = [[] for _ in range(N+1)]
    check = [0 for _ in range(N+1)]
    for _ in range(M):
        start_node, target_node = map(int, read_line().split())
        graph[start_node].append(target_node)
        
    for edges in graph:
        for edge in edges:
            check[edge] += 1
    
    topo = topology_sort(graph, check, N+1)
    
    print(*topo)
    
    
main()
