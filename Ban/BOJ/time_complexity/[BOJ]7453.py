'''
    https://www.acmicpc.net/problem/7453

    Binary search
    Sort
    Two pointer
'''
import sys; input_line = sys.stdin.readline
from itertools import combinations 

n = int(input_line())
abcd = [list(map(int, input_line().split())) for _ in range(n)]
result = 0

# Using dictionary
ab = dict()
for i in range(n):
    for j in range(n):
        v = abcd[i][0] + abcd[j][1]
        if v not in ab.keys():
            ab[v] = 1
        else:
            ab[v] += 1

for i in range(n):
    for j in range(n):
        v = -1 * (abcd[i][2] + abcd[j][3])
        if v in ab.keys():
            result += ab[v]
print(result)

#-----
## Using Sort and Two pointer
# ab, cd = [], []

# for i in range(n):
#     for j in range(n):
#         ab.append(abcd[i][0] + abcd[j][1])
#         cd.append(abcd[i][2] + abcd[j][3])

# ab.sort()
# cd.sort()

# start, end = 0, len(cd) - 1 # start point of ab, end point of cd (two pointer)
# while start < len(ab) and end >= 0:
#     if ab[start] + cd[end] == 0:
#         next_start, next_end = start + 1, end - 1

#         # next ab is same
#         while next_start < len(ab) and ab[start] == ab[next_start]:
#             next_start += 1
        
#         # next cd is same
#         while next_end >= 0 and cd[end] == cd[next_end]:
#             next_end -= 1
        
#         result += (next_start - start) * (end - next_end)
#         start, end = next_start, next_end
    
#     elif ab[start] + cd[end] > 0:
#         end -= 1
#     else:
#         start += 1

# print(result)