'''
    https://www.acmicpc.net/problem/1717

    Union-Find
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

# sys.stdin = open("data.txt", 'r')

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, read_line().split())
parent = [*range(N+1)]
UNION, FIND = 0, 1

for i in range(M):
    command, a, b = map(int, read_line().split())

    if command == UNION:
        union(parent, a, b)
    elif command == FIND:
        print("YES") if find(parent, a) == find(parent, b) else print("NO")
        