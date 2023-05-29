'''
    https://www.acmicpc.net/problem/5639

    Binary tree
'''
import sys
sys.setrecursionlimit(10 ** 5)
input_line = lambda: sys.stdin.readline().strip()

pre_order = []
while True:
    try:
        pre_order.append(int(input_line()))
    except:
        break
# Normal
def post_order(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if pre_order[start] < pre_order[i]:
            mid = i
            break
    post_order(start + 1, mid - 1)
    post_order(mid, end)
    print(pre_order[start])

post_order(0, len(pre_order)-1)


# # Using node class
# class Node():
#     def __init__(self, data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None

# class BinaryTree():
#     def __init__(self) -> None:
#         self.root = None

#     def insert(self, data):
#         node = Node(data)
#         if self.root == None:
#             self.root = node
#             return
#         parent = None
#         temp = self.root
#         while (temp != None):
#             parent = temp
#             if data < temp.data:
#                 temp = temp.left
#             elif temp.data <= data:
#                 temp = temp.right
#         if data < parent.data:
#             parent.left = node
#         else:
#             parent.right = node

#     # While
#     def post_order(self):
#         root = self.root
#         stack = []
#         while True:
#             while root != None:
#                 stack.append(root)
#                 stack.append(root)
#                 root = root.left
            
#             if not stack:
#                 return

#             root = stack.pop()
#             if stack and stack[-1] == root:
#                 root = root.right
#             else:
#                 print(root.data)
#                 root = None



#     # # Recursion
#     # def post_order(self, current):
#     #     if current:
#     #         self.post_order(current.left)
#     #         self.post_order(current.right)
#     #         print(current.data)
# binary_tree = BinaryTree()

# for i in range(0, len(pre_order)):
#     binary_tree.insert(pre_order[i])
# binary_tree.post_order()

# # # Recursion
# # binary_tree.post_order(binary_tree.root)

