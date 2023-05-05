'''
    https://www.acmicpc.net/problem/2805

    Binary search
'''
import sys

input_line = sys.stdin.readline

trees_num, tree_length = map(int, input_line().rstrip().split())
trees = list(map(int, input_line().rstrip().split()))

# Sequential search
def sequential_search(trees_num, tree_length, trees):
    max_height = max(trees)

    while max_height >= 0:
        max_height -= 1
        length_sum = 0
        for tree in trees:
            length_sum += max(tree - max_height, 0)

        if tree_length <= length_sum:
            print(max_height)
            break
    
# Bianry search
def bianry_search(trees_num, tree_length, trees):
    low, high = 0, max(trees)

    while low <= high:
        mid = (low + high) // 2

        length_sum = 0
        for tree in trees:
            if tree >= mid:
                length_sum += tree - mid

        if length_sum >= tree_length:
            low = mid + 1
        else:
            high = mid - 1
    
    print(high)

bianry_search(trees_num, tree_length, trees)