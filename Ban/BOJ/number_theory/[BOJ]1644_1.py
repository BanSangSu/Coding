'''
    https://www.acmicpc.net/problem/1644
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def get_primes(N):
    is_prime = [True for _ in range(N+1)]
    for i in range(3, int(N**0.5) + 1, 2):
        if is_prime[i]:
            is_prime[i*2::i] = [False] * len(is_prime[i*2::i])
    return [2] + [i for i in range(3, N+1, 2) if is_prime[i]]

def two_pointer(prime_list, target):
    start = 0
    end = 0
    value_sum = 0
    count = 0

    while True:
        if value_sum < target:
            if end == len(prime_list):
                break
            value_sum += prime_list[end]
            end += 1
        elif value_sum > target:
            value_sum -= prime_list[start]
            start += 1
        else:
            count += 1
            value_sum -= prime_list[start]
            start += 1
        
    return count


N = int(read_line())
prime_list = get_primes(N)

result = two_pointer(prime_list, N)
print(result)
