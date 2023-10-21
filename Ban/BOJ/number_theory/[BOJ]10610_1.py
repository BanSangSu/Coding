'''
    https://www.acmicpc.net/problem/10610
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = read_line()

def solution(N):
    A = 10
    count = [0] * A
    for i in N:
        count[int(i)] += 1
    if count[0] < 1:
        return -1
    d = 0
    for i in range(A):
        d += i*count[i]
    if d % 3: # d % 3 != 0
        return -1
    s = ""
    for i in range(9, -1, -1):
        s += str(i)*count[i]
    return s


print(solution(N))
