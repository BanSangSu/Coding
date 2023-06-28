'''
    https://www.acmicpc.net/problem/1256

    Dynamic Programming
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", "r")

N, M, K = map(int, read_line().split())
dp = [[1] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

if K > dp[N][M]:
    print(-1)
else:
    answer = ""
    while N > 0 and M > 0:
        split = dp[N-1][M]
        if K <= split: # next word is 'a'
            N -= 1
            answer += 'a'
        else: # next word is 'z'
            M -= 1
            K -= split # Remove impossible candidates
            answer += 'z'
    else:
        answer += ('a' * N + 'z' * M)
    print(answer)
