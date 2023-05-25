'''
    https://www.acmicpc.net/problem/10828

    Stack
'''
import sys; input_line = sys.stdin.readline

n_command = int(input_line())

stack = []

i = n_command 
while 0 < i:
    command = input_line().split()
    cmd = command[0]
    if cmd == "push":
        num = int(command[1])
        stack.append(num)
    elif cmd == "pop":
        print(stack.pop()) if stack else print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(1) if not stack else print(0)
    elif cmd == "top":
        print(stack[-1]) if stack else print(-1)
    else:
        print("Wrong command")
        i += 1

    i -= 1
