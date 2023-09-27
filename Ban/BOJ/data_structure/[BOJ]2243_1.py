'''
    https://www.acmicpc.net/problem/2243
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import math

sys.stdin = open("data.txt", 'r')

class Fenwick_tree:
    def __init__(self) -> None:
        self.size = 100_0000
        self.tree = [0 for _ in range(1 << math.ceil(math.log2(self.size))+1)]

    def update(self, idx, L, R, tar, val):
        if tar < L or R < tar: return self.tree[idx]
        if L == R:
            self.tree[idx] += val
            return self.tree[idx]
        
        mid = (L+R) // 2
        self.tree[idx] = self.update(2*idx, L, mid, tar, val) + self.update(2*idx+1, mid+1, R, tar, val)
        return self.tree[idx]

    def query(self, idx, L, R, val):
        self.tree[idx] -= 1
        if L == R: return L

        mid = (L+R)//2
        if val <= self.tree[2*idx]: return self.query(2*idx, L, mid, val)
        else: return self.query(2*idx+1, mid+1, R, val-self.tree[2*idx])

N = int(input_line())

fenwick_tree = Fenwick_tree()
for _ in range(N):
    A, *O = map(int, input_line().split())
    if A == 1: # Pick
        candy = fenwick_tree.query(1, 1, fenwick_tree.size, O[0])
        print(candy)
    elif A == 2: # Insert
        fenwick_tree.update(1, 1, fenwick_tree.size, O[0], O[1])
