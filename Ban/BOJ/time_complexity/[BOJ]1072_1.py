'''
    https://www.acmicpc.net/problem/1072
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

X, Y = map(int, input_line().split())
Z = int(100*Y/X)

if Z != 99 and Z != 100:
    answer = math.ceil((X*(Z+1)-100*Y)/(99-Z))

    print(answer)

else:
    print(-1)
