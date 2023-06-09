'''
    https://www.acmicpc.net/problem/2003

    Brute Force
    Two pointers
'''
import sys

def go (N, M, A):
    left, right = 0, 1
    cnt = 0
    while right <= N and left <= right:
        total = sum(A[left:right])

        if total < M:
            right += 1
        elif total > M:
            left += 1
        else:
            cnt += 1
            right += 1

    return cnt

input_line = sys.stdin.readline

N, M = map(int, input_line().rstrip().split())
A = list(map(int, input_line().rstrip().split()))

print(go(N, M, A))