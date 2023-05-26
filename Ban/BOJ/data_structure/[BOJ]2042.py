'''
    https://www.acmicpc.net/problem/2042

    Segment tree
'''
import sys; read_line = sys.stdin.readline
from math import ceil, log
# Segment tree
class Tree():
    def __init__(self, N, num_arr) -> None:
        self.num_arr = num_arr
        H = ceil(log(N, 2) + 1)
        self.segment_tree = [0] * (2**H) # index 1 == root
    
    def build(self, start, end, node):
        # if leaf node
        if start == end:
            self.segment_tree[node] = self.num_arr[start]
            return
        
        # left child node + right child node
        mid = (start+end) // 2
        self.build(start, mid, node*2)
        self.build(mid+1, end, node*2+1)
        self.segment_tree[node] = self.segment_tree[node*2] + self.segment_tree[node*2+1]
    
    # if num_arr is changed(diff), update segment_tree
    def update(self, start, end, node, update_node, diff):
        if not (start <= update_node <= end):
            return
        self.segment_tree[node] += diff

        if start == end:
            return

        mid = (start+end) // 2
        self.update(start, mid, node*2, update_node, diff)
        self.update(mid+1, end, node*2+1, update_node, diff)

    def query(self, start, end, node, left, right):
        # Sum of interval
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return self.segment_tree[node]
        mid = (start+end) // 2
        return self.query(start, mid, node*2, left, right) + self.query(mid+1, end, node*2+1, left, right)

N, M, K = map(int, read_line().split())

num_arr = [int(read_line()) for _ in range(N)]
segment_tree = Tree(N, num_arr)

segment_tree.build(0, N-1, 1)


for _ in range(M+K):
    a, b, c = map(int, read_line().split())

    if a == 1:
        b -= 1
        diff = c - segment_tree.num_arr[b]
        segment_tree.num_arr[b] = c
        segment_tree.update(0 , N-1, 1, b, diff)

    elif a == 2:
        b -= 1
        c -= 1
        print(segment_tree.query(0, N-1, 1, b, c))

# ---------------------------------
# # time out
# for i in range(M+K):
#     a, b, c = map(int, read_line().split())

#     if a == 1:
#         num_arr[b-1] = c
#     elif a == 2:
#         # range add
#         points = [b-1, c]
#         tmp_arr = num_arr[points[0]:points[1]]
#         print(sum(tmp_arr))
