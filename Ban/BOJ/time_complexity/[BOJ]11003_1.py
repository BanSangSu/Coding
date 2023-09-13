'''
    https://www.acmicpc.net/problem/11003
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
from collections import deque
# sys.stdin = open("data.txt", 'r')

N, L = map(int, input_line().split())
A = list(map(int, input_line().split()))

window = deque()
for i, v in enumerate(A):
    while window and v < A[window[-1]]:
        window.pop()
    window.append(i)
    if window and window[0] <= i - L:
        window.popleft()
    
    print(A[window[0]], end=' ')