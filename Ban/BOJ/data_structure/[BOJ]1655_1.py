'''
    https://www.acmicpc.net/problem/1655
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", 'r')

N = int(input_line())

min_heap, max_heap = [], []

for i in range(N):
    num = int(input_line())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and min_heap[0] < -max_heap[0]:
        min_value = heapq.heappop(min_heap)
        max_value = -heapq.heappop(max_heap)

        heapq.heappush(min_heap, max_value)
        heapq.heappush(max_heap, -min_value)

    print(-max_heap[0])
