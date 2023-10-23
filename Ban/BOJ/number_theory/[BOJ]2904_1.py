'''
    https://www.acmicpc.net/problem/2904
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def factorise(x):
    factors = {}
    if x > 1:
        for i in range(2, int(x**.5) + 1):
            while x % i == 0:
                x //= i
                factors[i] = factors.get(i, 0) + 1
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
    return factors


N = int(read_line())
a = [*map(int, read_line().split())]

D, P = {}, {}
for x in a:
    D[x] = factorise(x)
    for p in D[x]:
        P[p] = P.get(p, 0) + D[x][p]

for p in P:
    P[p] //= N

gcd = 1
for p in P:
    gcd *= p ** P[p]

cnt = 0
for i in a:
    for p in P:
        cnt += max(0, P[p] - D[i].get(p, 0))

print(gcd, cnt)