'''
    https://www.acmicpc.net/problem/10714
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
cakes = [int(read_line()) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[0][i] = cakes[i]

for i in range(N-1):
    for j in range(N):
        if i % 2 == 0:
            a = (j-1) % N
            b = (j+i+1) % N
            if cakes[a]  > cakes[b]:
                dp[i+1][a] = max(dp[i+1][a], dp[i][j])
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        else:
            if dp[i][j] == 0:
                continue
            a = (j-1) % N
            b = (j+i+1) % N
            dp[i+1][a] = max(dp[i+1][a], dp[i][j]+cakes[a])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+cakes[b])            
print(max(dp[N-1]))
