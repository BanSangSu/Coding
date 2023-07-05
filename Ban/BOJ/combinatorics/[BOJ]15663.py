'''
    https://www.acmicpc.net/problem/15663
    
    Backtracking
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())

N_nums = sorted(list(map(int, read_line().split())))

# DFS using Recursion
visited = [False for _ in range(N)]
tmp = []
def dfs(depth):
    stack = []
    if depth == M:
        print(*tmp)
        return 
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != N_nums[i]:
            visited[i] = True
            overlap = N_nums[i]
            tmp.append(N_nums[i])
            dfs(depth + 1)
            visited[i] = False
            tmp.pop()
dfs(0)