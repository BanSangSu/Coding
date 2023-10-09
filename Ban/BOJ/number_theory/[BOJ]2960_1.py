'''
    https://www.acmicpc.net/problem/2960
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, K = map(int, read_line().split())
sieve = [False] * (N + 1)
flag = False
tmp = 0
for i in range(2, N+1):
    for j in range(i, N + 1, i):
        if sieve[j] == False:
            sieve[j] = True
            tmp += 1
            if tmp == K:
                flag = True
                print(j)
                break
    if flag:
        break
