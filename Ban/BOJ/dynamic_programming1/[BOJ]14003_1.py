'''
    https://www.acmicpc.net/problem/14003

    Longest Increasing Subsequence (LIS)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

# sys.stdin = open("data.txt", 'r')

A = int(read_line())
sequence = list(map(int, read_line().split()))
LIS = []
dp = []
for x in sequence:
    if not LIS or LIS[-1] < x:
        LIS.append(x)
        dp.append((len(LIS)-1, x))
    else:
        idx = bisect_left(LIS, x)
        LIS[idx] = x
        dp.append((idx, x))

ans = []
last_idx = len(LIS) - 1
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        ans.append(dp[i][1])
        last_idx -= 1
print(len(ans))
print(*reversed(ans))