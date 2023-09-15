'''
    https://www.acmicpc.net/problem/10845
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
from collections import deque

# sys.stdin = open("data.txt", 'r')

n_commands = int(input_line())
deq = deque()

def execute(command):
    return {
        "push": lambda: deq.append(int(command[1])),
        "pop": lambda: deq.popleft() if deq else -1,
        "size": lambda: len(deq),
        "empty": lambda: 0 if deq else 1,
        "front": lambda: deq[0] if deq else -1,
        "back": lambda: deq[-1] if deq else -1,
    }.get(command[0], "Wrong Command!")()

for _ in range(n_commands):
    command = input_line().split()

    result = execute(command)
    if result != None:
        print(result)