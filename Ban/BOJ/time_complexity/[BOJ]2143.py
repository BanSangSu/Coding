'''
    https://www.acmicpc.net/problem/2143

    Prefix sum
    Binary search
'''
import sys; input_line = sys.stdin.readline
from bisect import bisect_left, bisect_right
from collections import Counter

T = int(input_line())
n = int(input_line())
a_array = list(map(int, input_line().split()))
m = int(input_line())
b_array = list(map(int, input_line().split()))

# Using Counter
result = 0
c = Counter()

for i in range(n):
    for j in range(i,n):
        c[sum(a_array[i:j+1])] += 1


for i in range(m):
    for j in range(i, m):
        t = T - sum(b_array[i:j+1])
        result += c[t]
print(result)

# Using bisect
# result = 0
# a_sum, b_sum = a_array, b_array
# for i in range(n):
#     for j in range(i+1, n):
#         a_sum.append(sum(a_array[i:j+1]))
# for i in range(m):
#     for j in range(i+1, m):
#         b_sum.append(sum(b_array[i:j+1]))

# a_sum.sort(); b_sum.sort()


# for i in range(len(a_sum)):
#     l = bisect_left(b_sum, T-a_sum[i])
#     r = bisect_right(b_sum, T-a_sum[i])
#     result += r-l
# print(result)