'''
    https://www.acmicpc.net/problem/13251
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

M = int(read_line())
C = list(map(int, read_line().split()))
K = int(read_line())

total_prob = math.comb(sum(C), K)
peddle_prob = 0
for c in C:
    peddle_prob += math.comb(c, K)

print(peddle_prob/total_prob)
