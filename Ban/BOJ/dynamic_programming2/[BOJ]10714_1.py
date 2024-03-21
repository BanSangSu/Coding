'''
    https://www.acmicpc.net/problem/10714
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
cake = [int(read_line()) for _ in range(N)]
dp = [[cake[j] if i == 0 else 0 for j in range(N)] for i in range(N)]

for i in range(1, N):
    for j in range(N):
        l = (j-1) % N
        r = (i+j) % N
        if i & 1 == 1:
            if cake[l] > cake[r]:
                dp[i][l] = max(dp[i][l], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
        else:
            if dp[i-1][j] == 0:
                continue
            dp[i][l] = max(dp[i][l], dp[i-1][j]+cake[l])
            dp[i][j] = max(dp[i][j], dp[i-1][j]+cake[r])
  
print(max(dp[-1]))