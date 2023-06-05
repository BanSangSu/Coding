'''
    https://www.acmicpc.net/problem/2243
    
    Fenwick Tree(Binary Index Tree)
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

class Fenwick_Tree:
    def __init__(self) -> None:
        self.size = 1000000
        self.tree = [0 for _ in range(self.size+1)]

    def update(self, _idx, _diff):
        while _idx <= self.size:
            self.tree[_idx] += _diff
            _idx += (_idx & -_idx)

    def get_sum(self, _idx):
        sum = 0
        while _idx > 0:
            sum += self.tree[_idx]
            _idx -= (_idx & -_idx)
        return sum
    
    def get_candy_idx(self, _pick):
        left, right = 1, self.size
        while left < right:
            mid = (left + right) // 2
            cum_candies = self.get_sum(mid)
            if _pick <= cum_candies: right = mid
            else: left = mid + 1

        return left

N = int(input_line())

fenwick_tree = Fenwick_Tree()
for _ in range(N):
    actions = [*map(int, input_line().split())]
    if actions[0] == 1: # Pick
        candy = fenwick_tree.get_candy_idx(actions[1])
        print(candy)
        fenwick_tree.update(candy, -1)

    elif actions[0] == 2: # Insert
        fenwick_tree.update(actions[1], actions[2])