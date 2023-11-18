'''
    https://www.acmicpc.net/problem/11438
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections.abc import Iterable, Sequence

# sys.stdin = open("data.txt", 'r')

subtree_size = [0] * 10

Tree = Sequence[Iterable[int]]


class LowestCommonAncestor:
    
    __slot__ = ('_parent', '_chain_top', '_depth')

    def __init__(self, tree: Tree, root: int = 0) -> None:
        self._parent = parent = [None] * len(tree)
        self._chain_top = top = list(range(len(tree)))
        self._depth = depth = [0] * len(tree)
        
        order = list(preorder(tree, root, parents=parent))
        subtree_size = [0] * len(tree)
        for u in reversed(order):
            subtree_size[u] = 1 + sum(map(subtree_size.__getitem__, tree[u]))
        for u in order[1:]:
            p = parent[u]
            depth[u] = depth[p] + 1
            subtree_size[p] = 0
            if subtree_size[u] > 1:
                heavy_child = max(tree[u], key=subtree_size.__getitem__)
                top[heavy_child] = top[u]
                
    def lca_node(self, u:int, v:int) -> int:
        u_top, v_top = self._chain_top[u], self._chain_top[v]
        while u_top != v_top:
            if self._depth[u_top] > self._depth[v_top]:
                u = self._parent[u_top]
                u_top = self._chain_top[u]
            else:
                v = self._parent[v_top]
                v_top = self._chain_top[v]
        return u if self._depth[u] < self._depth[v] else v
    
def preorder(tree:Tree, root:int = 0, *, parents: list[int] | None = None):
    stack = [root]
    parents = [None] * len(tree) if parents is None else parents
    while stack:
        u = stack.pop()
        yield u
        p = parents[u]
        for v in reversed(tree[u]):
            if v != p:
                parents[v] = u
                stack.append(v)
                
def main():
    N = int(read_line())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = [int(x) for x in read_line().split()]
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
        
    lca = LowestCommonAncestor(tree, 0)
    M = int(read_line())
    for _ in range(M):
        u, v = [int(x) for x in read_line().split()]
        print(lca.lca_node(u - 1, v - 1) + 1)
        
    
if __name__ == '__main__':
    main()
    