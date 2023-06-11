'''
    https://www.acmicpc.net/problem/1735
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

N = 2
numerators, denominators = [], []

for _ in range(N):
    numerator, denominator = map(int, read_line().split())
    numerators.append(numerator)
    denominators.append(denominator)

ans_numerator = numerators[0]* denominators[1] + numerators[1] * denominators[0] 
ans_denominator = denominators[0] * denominators[1]

# gcd = gcd(ans_numerator, ans_denominator)
gcd = math.gcd(ans_numerator, ans_denominator)

print(ans_numerator//gcd, ans_denominator//gcd)