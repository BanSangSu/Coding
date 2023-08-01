'''
    https://www.acmicpc.net/problem/14003

    Longest Increasing Subsequence (LIS)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

A = int(read_line())
sequence = list(map(int, read_line().split()))

# Binary search Bisect
from bisect import bisect_left
LIS = []
dp = []
for x in sequence:
    if not LIS or x > LIS[-1]:
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


# # Binary search Scratch 
# LIS = [sequence[0]]
# dp = [(0, sequence[0])]
# def binary_search(num):
#     start = 0
#     end = len(LIS) - 1

#     while start <= end:
#         mid = (start+end) // 2
        
#         if LIS[mid] == num:
#             return mid
#         elif LIS[mid] < num:
#             start = mid + 1
#         else:
#             end = mid -1

#     return start


# for i in range(1, A):
#     if sequence[i] > LIS[-1]:
#         dp.append((len(LIS), sequence[i]))
#         LIS.append(sequence[i])
#     else:
#         idx = binary_search(sequence[i])
#         LIS[idx] = sequence[i]
#         dp.append((idx, sequence[i]))

# print(len(LIS))
# last_idx = len(LIS) - 1
# result = []
# for i in range(len(dp)-1, -1, -1):
#     idx, num = dp.pop()
#     if idx == last_idx:
#         result.append(num)
#         last_idx -= 1

# print(*result[::-1])