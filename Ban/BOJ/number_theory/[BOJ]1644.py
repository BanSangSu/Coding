'''
    https://www.acmicpc.net/problem/1644

    Sieve of Eratosthenes
    Two Pointer
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

def get_prime(N):
    prime_list = list(range(N))

    for i in range(2, math.isqrt(N)+1):
        if prime_list[i]:
            prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

    return prime_list

N = int(read_line())
prime_list = get_prime(N+1)
prime_list = [prime for prime in prime_list[2:] if prime]

# Method 2
sum_prime = [0] * (len(prime_list)+1) # Meaningful data start from 1
for i in range(len(prime_list)):
    sum_prime[i+1] = sum_prime[i] + prime_list[i]

result_count = 0
start = 0
end = 1
while end < len(sum_prime):
    if sum_prime[end] - sum_prime[start] == N:
        result_count += 1
        start += 1
    elif sum_prime[end] - sum_prime[start] < N:
        end += 1
    else:
        start += 1

# # Method 1
# prime_list = prime_list + [0]

# result_count = 0
# start = 0
# end = 0
# sum_prime = prime_list[start]
# while end < len(prime_list)-1:
#     if sum_prime == N:
#         result_count += 1
#         sum_prime -= prime_list[start]
#         start += 1
#         end += 1
#         sum_prime += prime_list[end]
#     elif sum_prime < N:
#         end += 1
#         sum_prime += prime_list[end]
#     else:
#         sum_prime -= prime_list[start]
#         start += 1

print(result_count)