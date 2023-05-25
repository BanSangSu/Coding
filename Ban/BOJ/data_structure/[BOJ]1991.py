'''
    https://www.acmicpc.net/problem/1991

    Tree
'''
import sys; input_line = sys.stdin.readline
from collections import defaultdict
from dataclasses import dataclass

N = int(input_line())

@dataclass
class Tree_node:
    left_node: str
    right_node: str

class Tree:
    def __init__(self) -> None:
        self.tree_data = defaultdict(Tree_node)

    def insert(self, temps):
        self.tree_data[temps[0]]= Tree_node(temps[1], temps[2])

    def preorder(self, root):
        if root != ".":
            print(root, end='')
            self.preorder(self.tree_data[root].left_node)
            self.preorder(self.tree_data[root].right_node)

    def inorder(self, root):
        if root != ".":
            self.inorder(self.tree_data[root].left_node)
            print(root, end='')
            self.inorder(self.tree_data[root].right_node)

    def postorder(self, root):
        if root != ".":
            self.postorder(self.tree_data[root].left_node)
            self.postorder(self.tree_data[root].right_node)
            print(root, end='')

tree = Tree()
for _ in range(N):
    temps = list(input_line().split())
    tree.insert(temps)

tree.preorder('A')
print()
tree.inorder('A')
print()
tree.postorder('A')