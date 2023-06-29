'''
    https://www.acmicpc.net/problem/5568

    Backtracking
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from itertools import permutations

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
K = int(read_line())

cards = [read_line() for _ in range(N)]

result = set()

# Using backtracking
check = [0]*N
temp = []
def backtracking(depth):
    if depth == K:
        result.add("".join(temp))
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = 1
        temp.append(cards[i])

        backtracking(depth+1)

        check[i] = 0
        temp.pop()
backtracking(0)

# # Using permutations
# for perm in permutations(cards, K):
#     result.add("".join(perm))

print(len(result))