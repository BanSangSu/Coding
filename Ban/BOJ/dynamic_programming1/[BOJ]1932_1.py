'''
    https://www.acmicpc.net/problem/1932

    Dynamic Programming    
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

n = int(read_line())

triangle = [[*map(int, read_line().split())] for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j] 
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1] 
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))