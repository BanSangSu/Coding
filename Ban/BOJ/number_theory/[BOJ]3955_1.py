'''
    https://www.acmicpc.net/problem/3955
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def extended_gcd(a, b, k):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b != 0:
        q, w = a//b, a%b
        a = b
        b = w
        s, t = s0 - q*s1, t0 - q*t1,
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t

    t0 = (t0 % k + k) % K

    if a != 1 or t0 > 10**9:
        return "IMPOSSIBLE"

    return t0

T = int(read_line())
for _ in range(T):
    K, C = map(int, read_line().split())
    if C == 1:
        if K + 1 > 10**9:
            print("IMPOSSIBLE")
        else:
            print(K+1)
        continue
    if K == 1:
        print(1)
        continue
    answer = extended_gcd(K, C, K)
    print(answer)