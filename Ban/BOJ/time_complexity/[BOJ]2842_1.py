'''
    https://www.acmicpc.net/problem/2842
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
from collections import deque

# P = post office, K = house, . = pasture
# sys.stdin = open("data.txt", 'r')

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

N = int(input_line())

def bfs(x, y, left, right):
    dq = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dq.append([x, y])
    visited[x][y] = 1
    while dq:
        x, y, = dq.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if left <= heights[nx][ny] <= right and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append([nx, ny])

    for i, j in locations:
        if not visited[i][j]:
            return 0
    
    return 1

grid, locations = [], []
for i in range(N):
    row = [*input_line()]
    grid.append(row)
    for j, k in enumerate(row):
        if k == "P" or k == 'K':
            locations.append([i, j])

heights, tmp_set = [], set()
for i in range(N):
    row = [*map(int, input_line().split())]
    heights.append(row)
    for k in row:
        tmp_set.add(k)
tmp_list = [*sorted(tmp_set)]
l_min = min(tmp_list)
r_max = max(tmp_list)

l_max, r_min = sys.maxsize, 0
for i, j in locations:
    l_max = min(l_max, heights[i][j])
    r_min = max(r_min, heights[i][j])

lq, rq = [], []
for k in tmp_list:
    if l_min <= k <= l_max:
        lq.append(k)
    if r_min <= k <= r_max:
        rq.append(k)

ans = sys.maxsize
i, j = 0, 0
while i < len(lq) and j < len(rq):
    l_flag, r_flag = 0, 0
    if bfs(locations[0][0], locations[0][1], lq[i], rq[j]):
        tmp = rq[j]-lq[i]
        if ans > tmp:
            ans = tmp
        i += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            i += 1; j += 1
        else:
            j += 1
            r_flag = 1
print(ans)