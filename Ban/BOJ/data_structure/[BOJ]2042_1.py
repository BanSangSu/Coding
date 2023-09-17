'''
    https://www.acmicpc.net/problem/2042
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M, K = map(int, read_line().split())

def build_tree(arr, tree):
    for i in range(N):
        tree[i + N] = arr[i]

    for i in range(N - 1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


def update_tree(idx, v, tree):
    tree[idx + N] = v
    current = idx + N
    while current > 1:
        tree[current >> 1] = tree[current] + tree[current ^ 1]
        current >>= 1

def query_tree(low, high, tree):
    result = 0
    low += N
    high += N
    
    while low < high:
        if low & 1:
            result += tree[low]
            low += 1

        if high & 1:
            high -= 1
            result += tree[high]
        low >>= 1
        high >>= 1
    return result

arr = []
tree = [0 for _ in range(2*N)]
for _ in range(N):
    arr.append(int(read_line()))

build_tree(arr, tree)

for i in range(M+K):
    a, b, c = map(int, read_line().split())
    if a == 1:
        update_tree(b-1, c, tree)
    elif a == 2:
        print(str(query_tree(b-1, c, tree)))