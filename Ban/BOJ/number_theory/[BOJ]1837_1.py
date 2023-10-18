'''
    https://www.acmicpc.net/problem/1837
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", "r")

P, K = map(int, read_line().split())

result = K

if P % 2 == 0:
    result = 2
else:
    for i in range(3, K, 2):
        if P % i == 0:
            result = i
            break

if result < K:
    print(f"BAD {result}")
else:
    print("GOOD")