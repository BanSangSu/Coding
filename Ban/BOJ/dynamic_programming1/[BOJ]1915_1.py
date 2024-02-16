'''
    https://www.acmicpc.net/problem/1915
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open("data.txt", 'r')

n, m = map(int, read_line().split())        
grid = [[*map(int, read_line())] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] == 1:
            grid[i][j] += min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])
print(max(map(max, grid))**2)