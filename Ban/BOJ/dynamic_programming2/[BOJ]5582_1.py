'''
    https://www.acmicpc.net/problem/5582
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque

# sys.stdin = open("data.txt", 'r')

s1 = read_line()
s2 = read_line()

dq = deque()
ans = 0
for i in s1:
    dq.append(i)
    while "".join(dq) not in s2:
        dq.popleft()
    ans = max(ans, len(dq))
print(ans)