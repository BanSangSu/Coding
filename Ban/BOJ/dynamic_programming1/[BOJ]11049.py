'''
    https://www.acmicpc.net/problem/11049
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
MAX = sys.maxsize

matrices = [tuple(map(int, read_line().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

# Pythoon passed!
sizes = [size for size, _ in matrices]
sizes.append(matrices[-1][1])
for l  in range(1, N):
    for i in range(N-l):
        j = i + l
        size_ij = sizes[i] * sizes[j+1]
        m = min(min_ik + min_kj + size_ij * size_k for min_ik, min_kj, size_k in zip(dp[i][i:j], dp[j][i+1:j+1], sizes[i+1:j+1]))
        dp[i][j] = dp[j][i] = m
print(dp[0][-1])

# # Pypy passed!
# for l in range(N-1):
#     for i in range(N-1-l):
#         j = l+i+1
#         dp[i][j] = MAX
#         for k in range(i, j):
#             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrices[i][0]*matrices[k][1]*matrices[j][1])
# print(dp[0][-1])

# # Pypy passed shortest code
# r=range
# N=int(read_line())
# x,y=zip(*[map(int, read_line().split())for i in r(N)])
# m=[[0]*N for i in r(N)]
# for k in r(1,N):
#     for i in r(N-k):m[i][i+k]=min(m[i][w]+m[w+1][i+k]+x[i]*y[w]*y[i+k]for w in r(i,i+k))
# print(m[0][-1])