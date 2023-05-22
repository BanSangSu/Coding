'''
    https://www.acmicpc.net/problem/1072

    Binary search
'''
import sys; input_line = sys.stdin.readline
import math
X, Y = map(int, input_line().split()) # Game number and Win number
Z_func = lambda x, y: math.floor(100 * y / x) # == 100 * y // x
Z = Z_func(X, Y)
if Z >= 99:
    print(-1)
else:
    start, end = 1, 1000000000
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        t_X = X + mid
        t_Y = Y + mid
        if Z_func(t_X, t_Y) > Z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    print(answer)