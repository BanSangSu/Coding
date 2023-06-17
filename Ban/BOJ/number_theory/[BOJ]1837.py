'''
    https://www.acmicpc.net/problem/1837
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

sys.stdin = open("data.txt", "r")

P, K = map(int, read_line().split())

# If you use P, you have Overflow Error becasue biggest P is 10^100. So use K.
def get_prime_list(K):
    prime_list = list(range(K))

    for i in range(2, math.isqrt(K)+1): 
        if prime_list[i]:
            prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

    return prime_list

prime_list = get_prime_list(K+1)
prime_list = [prime for prime in prime_list[2:] if prime and prime < K]

for p in prime_list:
    if P % p == 0:
        print("BAD", p)
        break
else:
    print("GOOD")

