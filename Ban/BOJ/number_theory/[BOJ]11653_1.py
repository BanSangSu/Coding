'''
    https://www.acmicpc.net/problem/11653
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", "r")

def prime_factors(N):
    factors = []

    a = 2
    while N % a == 0:
        factors.append(a)
        N //= a

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i
    
    if N > 1:
        factors.append(N)

    return factors
    

N = int(read_line())

factors = prime_factors(N)
factors = map(str, factors)
print(f"\n".join(factors))