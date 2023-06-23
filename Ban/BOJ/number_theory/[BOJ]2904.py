'''
    https://www.acmicpc.net/problem/2904

'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

import math

# sys.stdin = open("data.txt", 'r')

def factorization(n, arr):
    # Sieve of Eratosthenes
    prime_list = [*range(n+1)]
    for i in range(2, math.isqrt(n)+1):
        if prime_list[i]:
            prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

    prime_list = [prime for prime in prime_list[2:] if prime]

    # Factorization
    factorization_dict = {}
    for a in arr:
        i = 0
        while a and i < len(prime_list):
            if a % prime_list[i] == 0:
                a //= prime_list[i]
                factorization_dict[prime_list[i]] = factorization_dict.get(prime_list[i], 0) + 1
            else:
                i += 1
    return factorization_dict

N = int(read_line())
arr = [*map(int, read_line().split())]
MAX = max(arr)
factorization_dict = factorization(MAX, arr)

gcd, min_moves = 1, 0
gcd_dict = {}
for k, v in factorization_dict.items():
    cnt = v//N
    gcd *= k ** (cnt)
    gcd_dict[k] = cnt

for a in arr:
    for k, v in gcd_dict.items():
        for i in range(v):
            if a % k == 0:
                a //= k
            else:
                min_moves += 1


print(gcd, min_moves)