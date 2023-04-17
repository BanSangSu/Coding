'''
    https://www.acmicpc.net/problem/1920
'''

import sys
import bisect
def input_line(): return sys.stdin.readline().strip()

N = input_line()
numbers_a = list(map(int, input_line().split()))
M = input_line()
numbers_b = list(map(int, input_line().split()))

numbers_a.sort()
for b in numbers_b:
    idx = bisect.bisect(numbers_a, b)
    print(1) if numbers_a[idx-1] == b else print(0)