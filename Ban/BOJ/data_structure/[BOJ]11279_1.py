'''
    https://www.acmicpc.net/problem/11279
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", "r")

N = int(input_line())

max_heap = []

for _ in range(N):
    x = int(input_line())
    if x == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -x)