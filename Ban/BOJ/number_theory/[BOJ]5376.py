'''
    https://www.acmicpc.net/problem/5376

'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()


# sys.stdin = open("data.txt", 'r')

N = int(read_line())

def gcd(x, y):
    while y:
        x, y = y, x%y
    return abs(x)

def solution(num):
    numerator, denominator = 1, 1
    start = num.find('(')
    if start == -1: #  Is not repeating decimal
        numerator = int(num[:1] + num[2:])
        denominator = int((10**(len(num[:1]) - 1)) * (10 ** len(num[2:])))
    else: # repeating decimal
        end = num.find(')')
        repeating_decimal = num[start+1:end]
        non_repeating = num[2:start]
        num1_left = 10 ** len(non_repeating + repeating_decimal)
        num2_left = 10 ** len(non_repeating)
        num1_right = non_repeating + repeating_decimal
        num2_right = non_repeating

        if num2_right == "": # all decimal is repeating
            num2_right = '0'
        
        numerator = int(int(num1_right) - int(num2_right))
        denominator = int(int(num1_left) - int(num2_left))
    return numerator, denominator


for i in range(N):
    num = read_line()
    numerator, denominator = solution(num)
    g = gcd(numerator, denominator)
    print(f"{numerator//g}/{denominator//g}")
    