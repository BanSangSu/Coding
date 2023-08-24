'''
    https://www.acmicpc.net/problem/1039

    BFS
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque

# sys.stdin = open("data.txt", 'r')

N, K = map(int, read_line().split())

def bfs(number, k):
    visited = {i:set() for i in range(1, k+1)}
    dq = deque([(number, 0)])
    length = len(number)

    while dq:
        num, cnt = dq.popleft()
        if cnt == k: continue
        for i in range(length):
            for j in range(i+1, length):
                temp = num[:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]
                if i == 0 and num[i] != '0' and num[j] == '0': continue
                if temp not in visited[cnt+1]:
                    visited[cnt+1].add(temp)
                    dq.append((temp, cnt+1))

    if visited[k]:
        return max(map(int, visited[k]))
    return -1

print(bfs(str(N), K))