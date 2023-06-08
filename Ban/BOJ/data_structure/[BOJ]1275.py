'''
    https://www.acmicpc.net/problem/1275

    Segment Tree
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from math import *

# sys.stdin = open("data.txt", 'r')

## Segment tree 
# Build
def build(node, start, end):
    if start == end:
        segment_tree[node] = arr[start]
        return segment_tree[node]
    
    mid = (start+end) // 2
    segment_tree[node] = build(node*2, start, mid) + build(node*2 + 1, mid+1, end)
    return segment_tree[node]

# Update
def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    
    segment_tree[node] += diff

    if not start == end:
        mid = (start+end) // 2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)

# Interval sum
def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return segment_tree[node]
    
    mid = (start+end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

if __name__ == "__main__":
    N, Q = map(int, read_line().split())

    arr = (list(map(int, read_line().split())))

    # Segment tree
    h = int(ceil(log2(N)))
    tree_size = 1 << (h+1)

    segment_tree = [0] * tree_size
    build(1, 0, N-1)

    for i in range(Q):
        x, y, index, value  = [*map(int, read_line().split())]

        if y < x:
            x, y = y, x
        print(query(1, 0 ,N-1, x-1, y-1))
        diff = value - arr[index-1]
        arr[index-1] = value
        update(1, 0, N-1, index-1, diff)