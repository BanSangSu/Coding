'''
    https://www.acmicpc.net/problem/2580
'''
import sys
def input_line(): return sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def dfs(depth, max_depth, N, board, row, col, square, zeros):
    if depth == max_depth:
        for i in range(N):
            print(*board[i])
        exit(0)

    nr, nc = zeros[depth]
    nsq = (nr//3)*3 + nc//3
    for i in range(1, 10):
        if not row[nr][i] and not col[nc][i] and not square[nsq][i]:
            row[nr][i] = True
            col[nc][i] = True
            square[nsq][i] = True
            board[nr][nc] = i
            dfs(depth+1, max_depth, N, board, row, col, square, zeros)
            row[nr][i] = False
            col[nc][i] = False
            square[nsq][i] = False
  

N = 9

board = [[False for _ in range(N)] for _ in range(N)]
row = [[False for _ in range(10)] for _ in range(N)]
col = [[False for _ in range(10)] for _ in range(N)]
square = [[False for _ in range(10)] for _ in range(N)]

zeros = []
for i in range(N):
    li = [*map(int, input_line().split())]
    for j in range(N):
        board[i][j] = li[j]
        if li[j]:
            row[i][li[j]] = True
            col[j][li[j]] = True
            square[(i//3)*3 + j//3][li[j]] = True
        else:
            zeros.append((i, j))
max_depth = len(zeros)

# result
dfs(0, max_depth, N, board, row, col, square, zeros)