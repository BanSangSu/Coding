'''
    https://www.acmicpc.net/problem/1102

    Bitmask, DFS, DP    
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')
INF = sys.maxsize

N = int(read_line())
generator = [[*map(int, read_line().split())] for _ in range(N)]
is_on = read_line()
reverse_is_on = is_on[::-1]

bit, count = 0, 0
for on in reverse_is_on:
    bit <<= 1
    if on == 'Y':
        bit |= 1
        count += 1

P = int(read_line())
dp = [INF for _ in range(1 << N)]


def dfs(bit, count, dp):
    if count >= P:
        return 0
    
    if dp[bit] != INF:
        return dp[bit]
    
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if bit & (1 << j) == 0:
                    dp[bit] = min(dp[bit], generator[i][j] + dfs(bit | 1 << j, count + 1, dp))

    return dp[bit]


ans = dfs(bit, count, dp)
print(-1 if ans == INF else ans)