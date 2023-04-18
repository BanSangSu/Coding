'''
    https://www.acmicpc.net/problem/9663

    Brute force
    Backtracking

'''
import sys

def is_primising(queens_position, now):
    for i in range(now):
        if queens_position[now] == queens_position[i] or abs(queens_position[now] - queens_position[i]) == abs(now-i):
            return False
    return True
def n_queen(queens_position, visited, N, now):
    count = 0
    if now == N:
        return 1
    else:
        for i in range(N):
            if visited[i]:
                continue

            queens_position[now] = i

            if is_primising(queens_position, now):
                visited[i]=True
                count += n_queen(queens_position, visited, N, now+1)
                visited[i]=False
    return count

N = int(sys.stdin.readline())
queens_position = N*[0]
visited = N*[False]

print(n_queen(queens_position, visited, N, 0))