'''
    https://www.acmicpc.net/problem/9663
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def n_queen(col, diagonal_l, diagonal_r, N, depth):
    ret = 0
    if depth >= N:
        return 1
    
    for c in range(N):
        if col[c] == 0 and diagonal_l[depth + c] == 0 and diagonal_r[N-1 + depth - c] == 0:
            col[c] = 1
            diagonal_l[c + depth] = 1
            diagonal_r[N-1 + depth - c] = 1
            ret += n_queen(col, diagonal_l, diagonal_r, N, depth + 1)

            col[c] = 0
            diagonal_l[c + depth] = 0
            diagonal_r[N-1 + depth - c] = 0
    return ret

N = int(read_line())
col = [0 for _ in range(N)]
diagonal_l = [0 for _ in range(2*N-1)]
diagonal_r = [0 for _ in range(2*N-1)]

cnt = n_queen(col, diagonal_l, diagonal_r, N, 0)
print(cnt)