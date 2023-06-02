'''
    https://www.acmicpc.net/problem/11279
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", "r")

N = int(input_line())

hq = []
heapq.heapify(hq)

for i in range(N):
    num = int(input_line())
    if num != 0:
        heapq.heappush(hq, -num)
    elif hq:
        tmp = -heapq.heappop(hq)
        print(tmp)
    else:
        print(0)