'''
    https://www.acmicpc.net/problem/11049
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
MAX = sys.maxsize

matrices = [tuple(map(int, read_line().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

sizes = [size for size, _ in matrices]
sizes.append(matrices[-1][1])

for l in range(1, N):
    for i in range(N-l):
        j = i + l
        size_ij = sizes[i] * sizes[j+1]
        m = min(min_ik + min_kj + size_ij * size_k for min_ik, min_kj, size_k in zip(dp[i][i:j], dp[j][i+1:j+1], sizes[i+1:j+1]))
        dp[i][j] = dp[j][i] = m
print(dp[0][-1])