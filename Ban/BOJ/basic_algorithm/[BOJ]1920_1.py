'''
    https://www.acmicpc.net/problem/1920
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
A = {i: 1 for i in map(int, read_line().split())}
M = int(read_line())
B = list(map(int, read_line().split()))

for j in B:
    print(A.get(j, 0))
    