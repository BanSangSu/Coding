'''
    https://www.acmicpc.net/problem/10845

    Queue
'''
import sys; input_line = sys.stdin.readline
from collections import deque

n_commands = int(input_line())
deq = deque()

i = n_commands


while 0 < i:
    command = input_line().split()
    cmd = command[0]
    if cmd == "push":
        deq.append(int(command[1]))
    elif cmd == "pop":
        print(deq.popleft()) if deq else print(-1)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "empty":
        print(0) if deq else print(1)
    elif cmd == "front":
        print(deq[0]) if deq else print(-1)
    elif cmd == "back":
        print(deq[-1]) if deq else print(-1)
    else:
        print("Wrong command.")
        i += 1
    i -= 1