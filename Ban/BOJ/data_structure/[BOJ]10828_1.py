'''
    https://www.acmicpc.net/problem/10828
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

n_command = int(input_line())

stack = []
for _ in range(n_command):
    c = input_line().split()

    if c[0] == "push":
        stack.append(int(c[1]))
    elif c[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == "size":
        print(len(stack))
    elif c[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
        