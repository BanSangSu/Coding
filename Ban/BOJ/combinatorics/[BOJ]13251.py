'''
    https://www.acmicpc.net/problem/13251

    Combination
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

M = int(read_line()) # the number of colors of pebbles
C = list(map(int, read_line().split())) # the nubmer of pebbles
K = int(read_line()) # the number of draws

num_each_pebble = 0
for pebble in C:
    num_each_pebble += math.comb(pebble, K)
num_all_pebbles = sum(C)
total = math.comb(num_all_pebbles, K)

print(num_each_pebble/total)
