'''
    https://www.acmicpc.net/problem/11062
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')


# The Code passed in Pypy
def find_score(N, cards):
    dp = [[None for _ in range(N)] for _ in range(N)]

    for i in range(N):
        dp_i, dp_j = 0, i
        for j in range(i, N):
            card = dp_j - dp_i + 1
            p_idx = (N + card) % 2
            
            try: case1 = int(dp[dp_i+1][dp_j])
            except: case1 = 0
            try: case2 = int(dp[dp_i][dp_j-1])
            except: case2 = 0

            if p_idx == 0:
                dp[dp_i][dp_j] = max(case1 + cards[dp_i], case2 + cards[dp_j])
            else:
                dp[dp_i][dp_j] = min(case1, case2)

            dp_i, dp_j = dp_i + 1, dp_j + 1

    return dp[0][-1]


T = int(read_line())
for _ in range(T):
    N = int(read_line())
    cards = [*map(int, read_line().split())]
    print(find_score(N, cards))

# # The Code passed in Python
# T = int(read_line())

# def solution(N, array):
#     dp = [[0 for _ in range(N)] for _ in range(N)]
#     n = N-1
#     r, w = 0, 1
#     if N % 2 == 0:
#         turn = True
#     else:
#         for i in range(N):
#             dp[i][i] = array[i]
#         turn = False
#     while n >= 1:
#         for k in range(n):
#             i = r+k
#             j = w+k
#             if turn:
#                 dp[i][j] = max(array[j] + dp[i][j-1], array[i] + dp[i+1][j])
#             else:
#                 dp[i][j] = min(dp[i][j-1], dp[i+1][j])
#         turn = not turn
#         n -= 1
#         w += 1
#     print(dp[0][-1])
    

# for _ in range(T):
#     N = int(read_line())
#     array = [*map(int, read_line().split())]
#     solution(N, array)