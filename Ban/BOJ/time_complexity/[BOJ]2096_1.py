'''
    https://www.acmicpc.net/problem/2096
'''
import sys
def input_line(): return sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(input_line())

table = [*map(int,input_line().split())]

dp_max = table
dp_min = table

for _ in range(N-1):
    table = [*map(int,input_line().split())]

    dp_max = [table[0]+max(dp_max[0],dp_max[1]), table[1]+max(dp_max), table[2]+max(dp_max[1],dp_max[2])]
    dp_min = [table[0]+min(dp_min[0],dp_min[1]), table[1]+min(dp_min), table[2]+min(dp_min[1],dp_min[2])]

print(max(dp_max), min(dp_min))