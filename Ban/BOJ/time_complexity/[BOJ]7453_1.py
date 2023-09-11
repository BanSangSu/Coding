'''
    https://www.acmicpc.net/problem/7453
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(input_line())
A, B, C, D = [], [], [], []
for _ in range(N):
    tmp = [*map(int, input_line().split())]
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])

AB = dict()
for a in A:
    for b in B:
        AB[a+b] = AB.get(a+b, 0) + 1

answer = 0
for c in C:
    for d in D: 
        answer += AB.get(-(c+d), 0)

print(answer)