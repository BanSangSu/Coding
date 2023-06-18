'''
    https://www.acmicpc.net/problem/2824

    Greatest Commmon Divisor
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def gcd(x, y):
    while y:
        x, y, = y, x % y
    return abs(x)

def mul(arr):
    ret = 1
    for i in arr:
        ret *= i
    return ret

N = int(read_line()) 
A_arr = map(int, read_line().split())
A = mul(A_arr)

M = int(read_line()) 
B_arr = map(int, read_line().split())
B = mul(B_arr)

result = str(gcd(A, B))
print(result[-9:])