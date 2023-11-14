'''
    https://www.acmicpc.net/problem/1717
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

# sys.stdin = open("data.txt", 'r')

class UnionFind():
    
    def __init__(self, size) -> None:
        self.parent = [-1 for _ in range(size+1)]

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        if self.parent[x] > self.parent[y]:
            self.parent[x] = y
        else:
            if self.parent[x] == self.parent[y]:
                self.parent[x] -= 1
            self.parent[y] = x
            
    def solution(self, cnt):
        for _ in range(cnt):
            command, a, b = map(int, read_line().split())
            root_a = self.find(a)
            root_b = self.find(b)
            
            if command == 0:
                if root_a != root_b:
                    self.union(root_a, root_b)
            elif command == 1:
                if root_a == root_b:
                    print("YES")
                else:
                    print("NO")
                    
            
if __name__ == "__main__":
    N, M = map(int, read_line().split())
    uf = UnionFind(N)
    uf.solution(M)