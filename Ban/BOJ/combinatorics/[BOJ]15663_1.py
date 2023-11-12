'''
    https://www.acmicpc.net/problem/15663
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

from itertools import permutations

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())

sorted_N = sorted(read_line().split(), key=int)
print("\n".join(map(" ".join, dict.fromkeys(permutations(sorted_N, M)))))

# visited = [False for _ in range(N)]
# tmp = []
# def dfs(depth):
#     prev = 0
#     if M == depth:
#         print(" ".join(map(str, tmp)))
#         return
    
#     for i in range(N):
#         if visited[i] == False and prev != sorted_N[i]:
#             visited[i] = True
#             tmp.append(sorted_N[i])
#             prev = sorted_N[i]
#             dfs(depth+1)
#             tmp.pop()
#             visited[i] = False

# dfs(0)