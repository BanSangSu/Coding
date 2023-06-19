'''
    https://www.acmicpc.net/problem/2725

    Greatest Common Divisor
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

C = int(read_line())

coordination = [0 for _ in range(1001)]
coordination[1] = 3
for x in range(2, 1001):
    cnt = 0
    for y in range(1, x+1):
        if x == y:
            continue
        if gcd(x, y) == 1:
            cnt += 2
    coordination[x] = coordination[x-1] + cnt

for _ in range(C):
    N = int(read_line())
    print(coordination[N])