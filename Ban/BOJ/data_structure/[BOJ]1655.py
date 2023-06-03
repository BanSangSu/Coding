'''
    https://www.acmicpc.net/problem/1655

    Priority queue
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", 'r')

N = int(input_line())

min_hq, max_hq = [], [] # multiply minus

for i in range(N):
    num = int(input_line())

    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, -num)
    else:
        heapq.heappush(min_hq, num)

    if min_hq and -max_hq[0] > min_hq[0]:
        max_value = -heapq.heappop(max_hq)
        min_value = heapq.heappop(min_hq)
        heapq.heappush(max_hq, -min_value)
        heapq.heappush(min_hq, max_value)

    print(-max_hq[0])