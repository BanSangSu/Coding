'''
    https://www.acmicpc.net/problem/2449
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

N, K = map(int, read_line().split())
bulbs = [0] + list(map(int, read_line().split()))

bulbs = [bulbs[i] for i in range(len(bulbs)) if i == 0 or bulbs[i] != bulbs[i-1]]
N = len(bulbs)

dp = [[INF for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    dp[i][i] = 0

for size in range(2, N):
    for start in range(1, N - size + 1):
        end = start + size - 1
        for mid in range(start, end):
            new_value = dp[start][mid] + dp[mid + 1][end]
            if bulbs[start] != bulbs[mid + 1]:
                new_value += 1
            dp[start][end] = min(dp[start][end], new_value)

print(dp[1][N-1])