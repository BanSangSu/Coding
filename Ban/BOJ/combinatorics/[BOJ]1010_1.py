'''
    https://www.acmicpc.net/problem/1010
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
# Idea: https://lee1201zxc.tistory.com/entry/%EB%B0%B1%EC%A4%80-1010-%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0C%EC%96%B8%EC%96%B4

# sys.stdin = open("data.txt", 'r')


def calc(N, M):
    left_side = 1
    right_side = 1
    for i in range(N):
        left_side *= (N-i)
        right_side *= (M-i)

    return right_side//left_side

T = int(read_line())

for _ in range(T):
    N, M = map(int, read_line().split())
    print(calc(N, M))
