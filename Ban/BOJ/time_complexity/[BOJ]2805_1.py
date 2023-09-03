'''
    https://www.acmicpc.net/problem/2805
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

sys.stdin = open("data.txt", 'r')

def bianry_search(N, M, trees):
    start, end = 0, max(trees)


    while start <= end:
        mid = (start + end) // 2
        
        total = 0
        for tree in trees:
            if tree > mid: 
                total += tree-mid

        if total < M:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


N, M = map(int, input_line().split())
trees = list(map(int, input_line().split()))

bianry_search(N, M, trees)