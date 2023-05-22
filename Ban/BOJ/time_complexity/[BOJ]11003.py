'''
    https://www.acmicpc.net/problem/11003

    Sliding Window
'''
import sys; input_line = sys.stdin.readline
from collections import deque

N, L = map(int, input_line().split())
A = list(map(int, input_line().split()))

deq = deque()

# Shortest code
# for i in range(N):
#     tmp = A[i]

#     while deq and deq[-1] > tmp: deq.pop()
#     deq.append(tmp)

#     # if i is bigger than L(window size)
#     if i >= L and deq[0] == A[i - L]: deq.popleft()
#     print(deq[0], end=' ')

# Popular code
d = [ 0 for i in range(N)]
for i in range(N):

    while deq and deq[-1][1] > A[i]:
        deq.pop()

    while deq and i - deq[0][0] >= L:
        deq.popleft()
    deq.append((i, A[i]))
    d[i] = deq[0][1]
print(*d)

