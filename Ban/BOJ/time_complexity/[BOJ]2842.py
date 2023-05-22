'''
    https://www.acmicpc.net/problem/2842

    BFS
    Two pointer
'''
import sys; input_line = sys.stdin.readline
from collections import deque

N = int(input_line())
# P = post office, K = house, . = pasture
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
graph, home = [], []
altitudes, temp_set = [], set()

def bfs(x, y, left, right):
    deq = deque()
    visited = [[0]*N for _ in range(N)]
    deq.append([x, y])
    visited[x][y] = 1
    while deq:
        x, y = deq.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if left <= altitudes[nx][ny] <= right and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    deq.append([nx, ny])

    for i, j in home:
        if not visited[i][j]:
            return 0
    return 1

# input
for i in range(N):
    row = list(input_line().rstrip())
    graph.append(row)
    for j, k in enumerate(row):
        if k == 'P' or k == 'K':
            home.append([i, j])

for i in range(N):
    row = list(map(int, input_line().split()))
    altitudes.append(row)
    for k in row:
        temp_set.add(k)
temp_list = list(sorted(temp_set))
l_min = min(temp_list)
r_max = max(temp_list)

l_max, r_min = sys.maxsize, 0
for i, j in home:
    l_max = min(l_max, altitudes[i][j])
    r_min = max(r_min, altitudes[i][j])

lq, rq = [], []
for k in temp_list:
    if l_min <= k <= l_max:
        lq.append(k)
    if r_min <= k <= r_max:
        rq.append(k)

answer = sys.maxsize
i, j = 0, 0
while i < len(lq) and j < len(rq):
    l_flag, r_flag = 0, 0
    if bfs(home[0][0], home[0][1], lq[i], rq[j]):
        answer = min(answer, rq[j] - lq[i])
        i += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            i += 1; j += 1
        else:
            j += 1
            r_flag = 1
            
print(answer)