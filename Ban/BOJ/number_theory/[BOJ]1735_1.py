'''
    https://www.acmicpc.net/problem/1735
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

a_numerator, a_denominator = map(int, read_line().split())
b_numerator, b_denominator = map(int, read_line().split())

numerator = (a_numerator*b_denominator) + (b_numerator*a_denominator)
denominator = a_denominator * b_denominator

# gcd = gcd(numerator, denominator)
gcd = math.gcd(numerator, denominator)
print(numerator // gcd, denominator // gcd)