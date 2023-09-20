'''
    https://www.acmicpc.net/problem/5639
'''
import sys
sys.setrecursionlimit(10 ** 5)
input_line = lambda: sys.stdin.readline().strip()

# sys.stdin = open("data.txt", 'r')

def postorder(start, end, tree):
    if start > end:
        return
    
    mid = start + 1
    node = tree[start]

    for i in range(start+1, end+1):
        if node < tree[i]:
            mid = i
            break
        
    postorder(start + 1, mid - 1, tree)
    postorder(mid, end, tree)
    print(node)

preorder = []
while True:
    try:
        preorder.append(int(input_line()))
    except:
        break

postorder(0, len(preorder) - 1, preorder)