'''
    https://www.acmicpc.net/problem/3020

    Binary search
    Prefix Sum
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

sys.stdin = open("data.txt", 'r')

N, H = map(int, read_line().split())

stalactite = [] 
stalagmite = []
for i in range(N):
    height = int(read_line())
    if i % 2 == 0:
        stalactite.append(height)
    else:
        stalagmite.append(height)

stalactite.sort()
stalagmite.sort()

cnt = 1
min_cnt = float('inf')
for h in range(1, H+1):
    
    # n - (stalac + stalag) = (n//2 - stalac) + (n//2 - stalag)
    stalac, stalag = bisect_left(stalactite, (H+1)-h), bisect_left(stalagmite, h) 
    total_cnt = N - (stalac + stalag)
    if total_cnt < min_cnt:
        min_cnt = total_cnt
        cnt = 1
    elif total_cnt == min_cnt:
        cnt += 1

print(min_cnt, cnt)
