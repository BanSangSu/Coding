'''
    https://www.acmicpc.net/problem/1202
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", "r")

N, K = map(int, input_line().split())

jewels = []
for _ in range(N):
    M, V = map(int, input_line().split())
    jewels.append((M, V))

bags = []
for _ in range(K):
    c = int(input_line())
    bags.append(c)

jewels.sort(reverse=True)
bags.sort()

carries = []
for m, v in jewels:
    if bags and m <= bags[-1]:
        del bags[-1]
        heapq.heappush(carries, v)
    elif carries:
        carry_v = heapq.heappop(carries)
        heapq.heappush(carries, v if v > carry_v else carry_v)

print(sum(carries))
