'''
    https://www.acmicpc.net/problem/2517
'''
import sys; input_line = sys.stdin.readline
from math  import ceil, log2
from bisect import bisect_left
## Python passed
def update_tree(i):
    while i <= M:
        tree[i] += 1
        i += i & -i
        
def sum_tree(i):
    SUM = 0
    while i:
        SUM += tree[i]
        i -= i&-i
    return SUM

N = int(input_line()); M = (1 << ceil(log2(500000)))
athletes = sorted([(int(input_line()),i) for i in range(1, N+1)], reverse=True)

tree = [0] * (M+1); result = [0]*N

for athlete, i in athletes:
    result[i-1] = sum_tree(i-1) + 1
    update_tree(i)

print(*result, sep='\n')


## Pypy passed
# def compress(athletes):
#     sorted_athletes = sorted(set(athletes))
#     return [bisect_left(sorted_athletes, x) for x in athletes]

# def update(node, start, end, idx, val):
#     tree[node] += val
#     if start != end:
#         mid = (start + end) >> 1
#         if idx <= mid:
#             update(node << 1, start, mid, idx, val)
#         else:
#             update(node << 1 | 1, mid+1, end, idx, val)

# def query(node, start, end, left, right):
#     if right < start or end < left:
#         return 0
#     if left <= start and end <= right:
#         return tree[node]
#     mid = (start + end) >> 1
#     return query(node << 1, start, mid, left, right) + query(node << 1 | 1, mid+1, end, left, right) 

# N = int(input_line())
# athletes = [int(input_line()) for _ in range(N)]
# athletes = compress(athletes)

# tree = [0] * (1 << ceil(log2(500000) + 1))
# for i in range(N):
#     print(i + 1 - query(1, 0, 499999, 0, athletes[i] - 1))
#     update(1, 0, 499999, athletes[i], 1)