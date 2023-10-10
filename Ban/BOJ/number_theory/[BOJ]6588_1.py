'''
    https://www.acmicpc.net/problem/6588
'''
import sys; read_line =  lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

MAX = 1000001

# Make sieve
sieve = [False]*2 + [True]*(MAX-2)
for i in range(3, int(MAX**0.5), 2):
    if sieve[i]:
        sieve[i*2::i] = [False]*((MAX-i-1)//i)

# Find prime list
prime = []
for i in range(3, MAX, 2):
    if sieve[i]:
        prime.append(i)

# Solve problems
while True:
    n = int(read_line())
    if not n:
        break

    for i in prime:
        if sieve[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
