'''
    https://www.acmicpc.net/problem/2143
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

# sys.stdin = open("data.txt", 'r')

T = int(input_line())
n = int(input_line())
a_array = list(map(int, input_line().split()))
m = int(input_line())
b_array = list(map(int, input_line().split()))

a_dict, b_dict = defaultdict(int), defaultdict(int)
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a_array[j]
        a_dict[temp] += 1

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b_array[j]
        b_dict[temp] += 1

answer = 0
for a in a_dict:
    b =  T - a
    if b in b_dict:
        answer += (a_dict[a] * b_dict[b])

print(answer)