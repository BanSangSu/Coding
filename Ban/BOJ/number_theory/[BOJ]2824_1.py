'''
    https://www.acmicpc.net/problem/2824
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from math import prod, gcd # prod is added from python 3.8
# sys.stdin = open("data.txt", 'r')

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# def prod(arr):
#     ret = 1
#     for a in arr:
#         ret *= a
#     return ret


N = int(read_line()) 
A_arr = map(int, read_line().split())
A = prod(A_arr)

M = int(read_line()) 
B_arr = map(int, read_line().split())
B = prod(B_arr)

result = str(gcd(A, B))
print(result[-9:])