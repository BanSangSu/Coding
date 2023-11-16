'''
    https://www.acmicpc.net/problem/1922
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
M = int(read_line())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
    
def union(parent, x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        

parent = [i for i in range(N+1)]
graph = []
answer = 0

for i in range(M):
    node_1, node_2, weight = map(int, read_line().split())
    graph.append((weight, node_1, node_2))
    
graph.sort(key=lambda x: x[0])
for cost, a, b in graph:
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        union(parent, a, b)
        answer += cost
        
print(answer)
