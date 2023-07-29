'''
    https://www.acmicpc.net/problem/1915
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open("data.txt", 'r')

n, m = map(int, read_line().split())

array = []
dp = [[0 for _ in range(m)]for _ in range(n)]
for _ in range(n):
   array.append(list(map(int, list(read_line()))))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = array[i][j]
        elif array[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        answer = max(dp[i][j], answer)

print(answer * answer)