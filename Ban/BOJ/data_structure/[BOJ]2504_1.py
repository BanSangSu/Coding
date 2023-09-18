'''
    https://www.acmicpc.net/problem/2504
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

parentheses  = list(input_line())

def check(parentheses):
    stack, result = [], ''
    flag = 0
    for p in parentheses:
        if p == '(':
            if flag == 1:
                result += '+'
            else:
                result += '('
            flag = 0
            stack.append(p)

        if p == ')':
            if flag == 0:
                result += '2'
            else:
                result += ')*2'
            flag = 1
            if not stack:
                return 0
            elif stack[-1] == '(':
                stack.pop()

        if p == '[':
            if flag == 1:
                result += '+'
            else:
                result += '('
            flag = 0
            stack.append(p)

        if p == ']':
            if flag == 0:
                result += '3'
            else:
                result += ')*3'
            flag = 1
            if not stack:
                return 0
            elif stack[-1] == '[':
                stack.pop()

    if stack:
        return 0
    else:
        result += ')'
        return eval(result)

print(check(parentheses))