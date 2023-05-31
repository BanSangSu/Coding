'''
    https://www.acmicpc.net/problem/1927
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", "r")
import heapq

N = int(input_line())

hq = []
heapq.heapify(hq)
for _ in range(N):
    num = int(input_line())
    if num != 0:
        heapq.heappush(hq, num)
    elif hq: 
        print(heapq.heappop(hq))
    else:
        print(0)