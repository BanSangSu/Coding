'''
    https://www.acmicpc.net/problem/3020

    IMOS
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, H = map(int, read_line().split())

def solve(H, limes):
    result, count = sys.maxsize, 0
    current = 0

    for i in range(H):
        current += limes[i]

        if result == current:
            count += 1
        elif result > current:
            result, count = current, 1

    return result, count


limes = [0 for _  in range(H)]

for i in range(N):
    l = int(read_line())

    # Stalagmite
    if i % 2:
        limes[H - l] += 1

    # Stalactite
    else:
        limes[0] += 1
        limes[l] -= 1

print(*solve(H, limes))