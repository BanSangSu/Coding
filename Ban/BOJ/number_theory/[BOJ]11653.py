'''
    https://www.acmicpc.net/problem/11653
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", "r")

N = int(read_line())

result = N

i = 2
while result > 1:
    if result % i == 0:
        print(i)
        result //= i
    else:
        i += 1
