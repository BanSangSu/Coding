'''
    https://www.acmicpc.net/problem/4358
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

trees = {}
num_tree = 0

# sys.stdin = open("data.txt", 'r')
while True:
    tree = input_line()
    if tree == '':
        break
    num_tree += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = sorted(trees.items(), key= lambda item: item[0])

for k, v in trees:
    percentage = v / num_tree * 100
    print(f"{k} {percentage:.4f}")