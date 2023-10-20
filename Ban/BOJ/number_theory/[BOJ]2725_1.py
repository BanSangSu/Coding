'''
    https://www.acmicpc.net/problem/2725
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def euler(n):
    ret = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            ret *= (1 - 1/i)
            while n % i == 0:
                n //= i
    if n != 1:
        ret *= (1 - 1/n)
    return int(ret)

A = 1000
coordination = [0] * A
coordination[0] = 3
for i in range(1, A):
    coordination[i] = coordination[i-1] + 2 * euler(i + 1)


C = int(read_line())
for _ in range(C):
    n = int(read_line())
    print(coordination[n-1])