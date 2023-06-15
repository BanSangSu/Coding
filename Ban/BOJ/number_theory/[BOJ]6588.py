'''
    https://www.acmicpc.net/problem/6588

    Prime number
    Sieve of Eratosthenes
'''
import sys; read_line =  lambda: sys.stdin.readline().rstrip()

import math

# sys.stdin = open("data.txt", 'r')

n = 1000000

# Different version
def get_prime_2(n):
    primes =  [*range(n)]
    for i in range(2, math.isqrt(n)+1):
        if primes[i]:
            primes[i+i::i] = [0] * len(primes[i+i::i])

    return primes

prime_list = get_prime_2(n+1)

prime_list = list(filter(None, prime_list[2:]))
# prime_list = [prime for prime in prime_list[2:] if prime]
prime_set = set(prime_list)

while num := int(read_line()):
    for a in prime_list:
        b = num - a
        if b in prime_set:
            print(f"{num} = {a} + {b}")
            break
                
    else:
        print("Goldbach's conjecture is wrong.")

# ####

# # Normal version => Time out! Because of finding a and b!(prime function is OK.)
# def get_prime_1(n):
#     primes =  [True] * n
#     for i in range(2, math.isqrt(n)+1):
#         if primes[i]:
#             for j in range(i+i, n, i):
#                 primes[j] = False

#     return primes

# prime_list = get_prime_1(n+1)
# while True:
#     num = int(read_line())
#     if num == 0:
#         break
#     for i in range(3, len(prime_list)):
#         if prime_list[i] and prime_list[num - i]:
#             print(f"{num} = {i} + {num-i}")
#             break
#     else:
#         print("Goldbach's conjecture is wrong.")
