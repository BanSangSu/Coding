'''
    https://www.acmicpc.net/problem/2517
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open("data.txt", 'r')

N = int(input_line())

mapper = {}
atheletes = []
for i in range(N):
    input_temp = int(input_line())
    atheletes.append(input_temp)
    mapper[input_temp] = i

atheletes.sort()

composition = [0 for _ in range(N)]
for i in range(N):
    composition[mapper[atheletes[i]]] = i

count = [0 for _ in range(N)]
ans = [0 for _ in range(N)]
for i in range(N):
    rank = i + 1
    j = composition[i]
    while j > 0:
        rank -= count[j-1]
        j &= j - 1

    ans[i] = rank
    j = composition[i]
    while j < N:
        count[j] += 1
        j |= j + 1

print('\n'.join(map(str, ans)))