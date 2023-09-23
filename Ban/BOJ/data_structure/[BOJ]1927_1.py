'''
    https://www.acmicpc.net/problem/1927
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

import heapq
# sys.stdin = open("data.txt", "r")

N = int(input_line())

min_heap = []
for _ in range(N):
    x = int(input_line())
    if x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)