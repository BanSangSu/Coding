'''
    https://www.acmicpc.net/problem/3830

    Union-Find
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# sys.stdin = open("data.txt", 'r')

def find(x, parent, weights):
    if x != parent[x]:
        # weights[x] = weights[x] + weights[parent[x]]
        # and then update parent of x(parent[x]) to find(parent[x])~~.
        p_find = find(parent[x], parent, weights)
        weights[x] += weights[parent[x]]
        parent[x] = p_find
    return parent[x]

def union(a, b, w, parent, weights):
    a_find = find(a, parent, weights)
    b_find = find(b, parent, weights)

    if a_find != b_find: 
        parent[b_find] = a_find
        weights[b_find] = weights[a] - weights[b] + w

while True:
    N, M = map(int, read_line().split())
    if [N, M] == [0, 0]:
        break

    weights = [0 for _ in range(N+1)]
    parent = [i for i in range(N+1)]
    for i in range(M):
        tmp = read_line().split()
        if tmp[0] == '!':
            a, b, w = map(int, tmp[1:]) 
            union(a, b, w, parent, weights)
        elif tmp[0] == '?':
            a, b = map(int, tmp[1:])
            a_find = find(a, parent, weights)
            b_find = find(b, parent, weights)
            if a_find == b_find:
                print(weights[b] - weights[a])
            else:
                print("UNKNOWN")
    print(weights)
