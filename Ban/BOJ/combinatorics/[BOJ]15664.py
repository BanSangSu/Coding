'''
    https://www.acmicpc.net/problem/15664

    Backtracking
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())
N_nums = sorted(list(map(int, read_line().split())))

visited = [False for _ in range(N)]
tmp = []
def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return
    
    overlap = 0
    for i in range(start, N):
        if not visited[i] and overlap != N_nums[i]:
            visited[i] = True
            tmp.append(N_nums[i])
            overlap = N_nums[i]
            dfs(i + 1)
            visited[i] = False
            tmp.pop()

dfs(0)
