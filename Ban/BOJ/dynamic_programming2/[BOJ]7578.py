'''
    https://www.acmicpc.net/problem/7578

    Fenwick tree -> Python code
    Segment tree -> Pypy code
'''
import sys; read_line =  lambda: sys.stdin.readline().rstrip()

from math import *

# sys.stdin = open("data.txt", 'r')

## Passed code in Python
def locate(m, idx):
    acc_num = 0
    k = idx
    while 0 < k:
        acc_num += fenwick_tree[k]
        k -= k & -k

    k = idx
    while k <= N:
        fenwick_tree[k] += 1
        k += k & -k

    return m - acc_num

N = int(read_line())
fenwick_tree = [0 for _ in range(N+1)]
loc = {}
count = 0

# machine A
for i, a in enumerate(map(int, read_line().split())):
    loc[a] = i+1

# machine B
for i, b in enumerate(map(int, read_line().split())):
    count += locate(i, loc[b])

print(count)

# ## Passed code in Pypy
# # Update visit count
# def update(node, start , end, idx):
#     if idx < start or end < idx:
#         return 0
    
#     if start == end:
#         tree[node] = 1
#         return tree[node]
    
#     mid = (start + end) // 2
#     update(node*2, start, mid, idx)
#     update(node*2+1, mid + 1, end, idx)
#     tree[node] = tree[node*2] + tree[node*2+1]
#     return tree[node]

# # Prefix sum
# def query(node, start, end, left, right):
#     if right < start or end < left:
#         return 0
    
#     if left <= start and end <= right:
#         return tree[node]
    
#     mid = (start + end) // 2
#     return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

# if __name__ == "__main__":
#     N = int(read_line())
#     A_machines = list(map(int, read_line().split()))

#     # Init B_machines dict
#     B_machines = {}
#     idx = 0
#     for num in map(int, read_line().split()):
#         B_machines[num] = idx
#         idx += 1
    
#     # Segment tree
#     h = int(ceil(log2(N)))
#     tree_size = 1 << (h+1)

#     tree = [0 for _ in range(tree_size)]

#     ans = 0
#     for num in A_machines:
#         s_idx = B_machines[num]
#         ans += query(1, 0, N-1, s_idx, N-1)

#         update(1, 0, N-1, s_idx)

#     print(ans)