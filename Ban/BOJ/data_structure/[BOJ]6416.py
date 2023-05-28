'''
    https://www.acmicpc.net/problem/6416
'''
import sys; input_readline = sys.stdin.readline
# from collections import defaultdict

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.child = None
#         self.parent = None
#     def __str__(self) -> str:
#         return str(self.data)
   
# nodes = defaultdict(list)
k = 1
nums = set()
nodes = []
while True:
    
    inputs = list(map(int, input_readline().split()))

    if not inputs:
        continue
    if inputs[0] == -1:
        break

    check = False
    if inputs[-1] == 0:
        inputs.pop()
        inputs.pop()
        check = True
    for i in range(0, len(inputs), 2):
        nodes.append(inputs[i+1])
    for input in inputs:
        nums.add(input)

    if check:
        is_tree = " "
        if not nodes:
            is_tree = " "
        else:
            nums = list(nums)
            n = len(nums)
            nums_dict  = {nums[i]: i for i in range(n)}

            indegree = [0] * n
            for node in nodes:
                w = nums_dict[node]
                indegree[w] += 1

            not_cycle0 = not_cycle1 = 0
            for i in range(n):
                if indegree[i] == 0:
                    not_cycle0 += 1
                elif indegree[i] == 1:
                    not_cycle1 += 1
            if not_cycle0 == 1 and not_cycle1 == n - 1:
                is_tree = ' '
            else:
                is_tree = ' not '

        print(f"Case {k} is{is_tree}a tree.")
        nums = set()
        nodes = []

        k += 1