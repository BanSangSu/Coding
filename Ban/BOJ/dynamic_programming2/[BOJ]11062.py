'''
    https://www.acmicpc.net/problem/11062
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open("data.txt", 'r')

# In Pypy, this code always passed, but in Python, timeout error was happened sometimes.... (I don't know why....)

def card_game(N, array):
    dp = [[None for _ in range(N)]for _ in range(N)]

    for i in range(N):
        dp_i, dp_j = 0, i
        for j in range(i, N):
            cards = dp_j - dp_i + 1
            p_idx = (N + cards) % 2
            # p_idx: Who's turn
            # 0 = G, 1 = M
            
            # Check whether value is None or error(out of index).
            try: case1 = int(dp[dp_i+1][dp_j])
            except: case1 = 0
            try: case2 = int(dp[dp_i][dp_j-1])
            except: case2 = 0

            # turn for G
            if p_idx == 0:
                dp[dp_i][dp_j] = max(case1 + array[dp_i], case2 + array[dp_j])
            # turn for M
            else:
                dp[dp_i][dp_j] = min(case1, case2)

            dp_i, dp_j = dp_i+1, dp_j+1

    return dp[0][N-1]

T = int(read_line())
for _ in range(T):
    N = int(read_line())
    array = list(map(int, read_line().split()))
    print(card_game(N, array))
