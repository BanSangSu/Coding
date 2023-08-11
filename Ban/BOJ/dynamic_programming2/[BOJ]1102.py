'''
    https://www.acmicpc.net/problem/1102

    Bitmask, DFS, DP    
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')
INF = sys.maxsize

N = int(read_line())
generators = []
for _ in range(N):
    generators.append(list(map(int, read_line().split())))
# status = [1 if s == "Y" else 0 for s in [*read_line()]]

mask = read_line()
mask = mask[::-1]
bit, count = 0, 0
for m in mask:
    bit <<= 1
    if m == 'Y':
        bit |= 1
        count += 1
P = int(read_line())
dp = [INF for _ in range(1 << N)]

def dfs(bit, cnt, dp):
    if cnt >= P:
        return 0
    
    if dp[bit] != INF:
        return dp[bit]
    
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if bit & (1 << j) == 0:
                    dp[bit] = min(dp[bit], generators[i][j] + dfs(bit | 1 << j, cnt + 1, dp))

    return dp[bit]

ans = dfs(bit, count, dp)
print(-1 if ans == INF else ans)