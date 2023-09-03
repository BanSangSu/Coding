'''
    https://www.acmicpc.net/problem/2003
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def go(N, M, A):
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


N, M = map(int, input_line().split())
A = list(map(int, input_line().split()))
print(go(N, M, A))

## Faster version!
# l,r,cnt,total = 0,0,0,0
# while True:
#     if M < total:
#         total -= A[l]
#         l += 1
#     elif r == N:
#         break
#     else:
#         total += A[r]
#         r += 1

#     if M == total:
#         cnt += 1

# print(cnt)