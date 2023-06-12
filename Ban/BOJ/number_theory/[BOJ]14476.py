'''
    https://www.acmicpc.net/problem/14476
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
nums =  list(map(int, read_line().split()))
prefix_gcds = [0] * (N+1)
suffix_gcds = [0] * (N+1)

prefix_gcds[0] = nums[0]
for i in range(1, N):
    prefix_gcds[i] = math.gcd(prefix_gcds[i-1], nums[i])

suffix_gcds[N-1] = nums[N-1]
for i in range(N-2, -1, -1):
    suffix_gcds[i] = math.gcd(suffix_gcds[i+1], nums[i])

ans = []
for i in range(N):
    left = prefix_gcds[i-1]
    right = suffix_gcds[i+1]

    res = math.gcd(left, right)
    
    if nums[i] % res == 0:
        continue
    ans.append((res, nums[i]))

ans.sort(reverse=True)
print(' '.join(map(str, ans[0])) if ans else -1)