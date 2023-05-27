'''
    https://www.acmicpc.net/problem/2504

    Stack
'''
import sys; input_line = sys.stdin.readline

temp  = list(input_line().rstrip())

stack = []
val = 1
answer = 0

for i, t in enumerate(temp):
    if t == '(':
        stack.append(t)
        val *= 2
    elif t == '[':
        stack.append(t)
        val *= 3
    elif t == ')':
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if temp[i-1] == '(':
            answer += val
        stack.pop()
        val //= 2
    elif t == ']':
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if temp[i-1] == '[':
            answer += val
        stack.pop()
        val //= 3

if stack:
    print(0)
else:
    print(answer)