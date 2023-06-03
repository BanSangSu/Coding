'''
    https://www.acmicpc.net/problem/1202

    Greedy
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", "r")

N, K = map(int, input_line().split())

# Weight and Value
jewelleries = [[*map(int, input_line().split())] for _ in range(N)]

max_weights = [int(input_line()) for _ in range(K)]

jewelleries.sort(); max_weights.sort()

result = 0
tmp_jew = []
for weight in max_weights:
    while jewelleries and weight >= jewelleries[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jewelleries)[1])
    
    if tmp_jew:
        result -= heapq.heappop(tmp_jew)
print(result)
