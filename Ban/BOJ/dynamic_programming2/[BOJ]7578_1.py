'''
    https://www.acmicpc.net/problem/7578

    Fenwick tree
'''
import sys; read_line =  lambda: sys.stdin.readline().rstrip()

from math import *

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
def locate(idx, location, fenwick_tree):
    cumulative_sum = 0
    k = location
    while 0 < k: # Sum
        cumulative_sum += fenwick_tree[k]
        k -= k & -k

    k = location
    while k <= N: # Add (update) 
        fenwick_tree[k] += 1
        k += k & -k
        
    return idx - cumulative_sum


fenwick_tree = [0 for _ in range(N+1)]
loc = {}
cnt = 0

for i, a in enumerate(map(int, read_line().split())):
    loc[a] = i + 1

for i, b in enumerate(map(int, read_line().split())):
    cnt += locate(i , loc[b], fenwick_tree)

print(cnt)