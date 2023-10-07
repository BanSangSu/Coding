'''
    https://www.acmicpc.net/problem/14476
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

sys.stdin = open("data.txt", 'r')

N = int(read_line())
nums =  list(map(int, read_line().split()))

gcd_list = [0] * N
gcd_list[1] = nums[0]
res = idx = -1
for i in range(1, N-1):
    gcd_list[i+1] = math.gcd(gcd_list[i], nums[i])
    if gcd_list[i+1] == math.gcd(gcd_list[i+1], nums[i]):
        gcd_list[i+1] = -1

temp = nums[-1]
if temp > res:
    res = gcd_list[-1]
    idx = N-1
for i in range(N-1, 0, -1):
    temp = math.gcd(temp, nums[i])
    if gcd_list[i-1] == -1:
        continue
    gcd_list[i-1] = math.gcd(gcd_list[i-1], temp)
    if gcd_list[i-1] == math.gcd(nums[i-1], gcd_list[i-1]):
        gcd_list[i-1] = -1
    if gcd_list[i-1] > res:
        res = gcd_list[i-1]
        idx = i-1

if res >= 0:
    print(res, nums[idx])
else:
    print(res)
    