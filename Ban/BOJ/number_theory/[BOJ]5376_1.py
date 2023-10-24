'''
    https://www.acmicpc.net/problem/5376
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import math

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

def solution(num):
    numerator, denominator = 1, 1
    start = num.find("(")
    if start == -1:
        numerator = int(num[2:])
        denominator = int(10**(len(num[2:])))
    else:
        end = num.find(")")
        non_repeating = num[2:start]
        repeating_decimal = num[start+1:end]
        
        num1_left = 10 ** len(non_repeating + repeating_decimal)
        num2_left = 10 ** len(non_repeating)
        num1_right = non_repeating + repeating_decimal
        num2_right = non_repeating

        if num2_right == "":
            num2_right = '0'
            
        numerator = int(int(num1_right) - int(num2_right))
        denominator = int(int(num1_left) - int(num2_left))
    return numerator, denominator

for _ in range(N):
    num = read_line()
    numerator, denominator = solution(num)
    g = math.gcd(numerator, denominator)
    print(f"{numerator//g}/{denominator//g}")