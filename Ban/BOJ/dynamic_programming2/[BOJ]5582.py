'''
    https://www.acmicpc.net/problem/5582
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

sys.stdin = open("data.txt", 'r')

str1 = read_line()
str2 = read_line()

# Code2 passed in Python
from collections import deque

q = deque()
ans = 0
for i in str1:
    q.append(i)
    while "".join(q) not in str2:
        q.popleft()
    ans = max(ans, len(q))
print(ans)


# # Code1 passed in Python
# dp = [0 for _ in range(len(str2)+1)]

# ans = 0
# for i in range(len(str1)):
#     dp1 = [0 for _ in range(len(str2)+1)]
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             dp1[j+1] = dp[j]+1
#             ans = max(ans, dp1[j+1])
#     dp = dp1
# print(ans)


# # Code passed in Pypy!
# dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

# answer = 0
# for i in range(1, len(dp)):
#     for j in range(1, len(dp[0])):
#         if str1[i-1] == str2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#             answer = max(answer, dp[i][j])
# print(answer)