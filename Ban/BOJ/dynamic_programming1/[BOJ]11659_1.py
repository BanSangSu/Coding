'''
    https://www.acmicpc.net/problem/11659

    Prefix sum
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())
arr = list(map(int, read_line().split()))

prefix_sum = [0 for _ in range(N+1)]
prefix_sum[1] = arr[0]

for i in range(2, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for _ in range(M):
    start, end = map(int, read_line().split())
    print(prefix_sum[end] - prefix_sum[start-1])