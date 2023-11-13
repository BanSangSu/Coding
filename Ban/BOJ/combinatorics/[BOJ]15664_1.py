'''
    https://www.acmicpc.net/problem/15664
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())
sorted_N = sorted(list(map(int, read_line().split())))

visited = [False for _ in range(N)]

tmp = []
def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return
    
    prev = 0
    for i in range(start, N):
        if not visited[i] and prev != sorted_N[i]:
            visited[i] = True
            tmp.append(sorted_N[i])
            prev = sorted_N[i]
            dfs(i+1)
            visited[i] = False
            tmp.pop()
            
dfs(0)
