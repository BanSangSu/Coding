'''
    https://www.acmicpc.net/problem/10610

'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = read_line()
n_arr = list(map(int, N))

sum_arr = sum(n_arr)

if sum_arr % 3 == 0:
    n_arr.sort(reverse=True)
    if n_arr[-1] == 0:
        print(''.join(list(map(str, n_arr))))
    else:
        print(-1)
else:
    print(-1)