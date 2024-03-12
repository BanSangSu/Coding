'''
    https://www.acmicpc.net/problem/9252

    Longest Common Subsequence (LCS)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

str1 = read_line()
str2 = read_line()

dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def find_str():
    answer = ""

    i = len(dp)-1
    j = len(dp[0])-1
    while i != 0 and j != 0:
        if dp[i][j-1] == dp[i][j]:
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1
        else:
            answer = str1[i-1] + answer
            j -= 1; i -= 1

    return answer

print(dp[-1][-1])
print(find_str())