'''
    https://www.acmicpc.net/problem/1991
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

# sys.stdin = open("data.txt", 'r')

N = int(input_line())

class Node():
    def __init__(self, data) -> None:
        self.data = data[0]
        self.left = data[1]
        self.right = data[2]

class Tree():
    def __init__(self) -> None:
        self.tree_data = defaultdict(Node)
    
    def insert(self, node):
        self.tree_data[node[0]] = Node(node)

    def preorder(self, data):
        if data != '.':
            print(data, end='')
            self.preorder(self.tree_data[data].left)
            self.preorder(self.tree_data[data].right)
    def inorder(self, data):
        if data != '.':
            self.inorder(self.tree_data[data].left)
            print(data, end='')
            self.inorder(self.tree_data[data].right)

    def postorder(self, data):
        if data != '.':
            self.postorder(self.tree_data[data].left)
            self.postorder(self.tree_data[data].right)
            print(data, end='')

tree = Tree()
for _ in range(N):
    tmp = input_line().split()
    tree.insert(tmp)

tree.preorder('A')
print()
tree.inorder('A')
print()
tree.postorder('A')