'''
    https://www.acmicpc.net/problem/2094
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())

def max_segment(start, end, node, tree, data):
    if start == end:
        tree[node] = data[start-1][1]
    else:
        mid = (start+end)//2
        tree[node] = max(max_segment(start, mid, node*2, tree, data), max_segment(mid+1, end, node*2 + 1, tree, data))
    return tree[node]

def search(year, data):
    start = 1
    end = N
    while start < end:
        mid = (start+end) // 2
        if year > data[mid-1][0]:
            start = mid+1
        else:
            end = mid
    if data[start-1][0] == year:
        return data[start-1][1], start
    else:
        return -1, start

def query(start, end, node, left, right, tree):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start+end) // 2
        return max(query(start, mid, node*2, left, right, tree), query(mid+1, end, node*2 + 1, left, right, tree))
    

data = [tuple(map(int, read_line().split())) for _ in range(N)]

tree = [0]*N*4
max_segment(1, N, 1, tree, data)


M = int(read_line())
for _ in range(M):
    Y, X = map(int, read_line().split())
    rain_y, node_y = search(Y, data)
    rain_x, node_x = search(X, data)

    if rain_x == -1 and rain_y == -1:
        print("maybe")
    elif rain_x == -1:
        if query(1, N, 1, node_y+1, node_x-1, tree) < rain_y:
            print("maybe")
        else:
            print("false")
    elif rain_y == -1:
        if query(1, N, 1, node_y, node_x-1, tree) < rain_x:
            print("maybe")
        else:
            print("false")       
    else:
        if rain_x > rain_y or query(1, N, 1, node_y+1, node_x-1, tree) >= rain_x:
            print("false")
        elif not X-Y == node_x-node_y:
            print("maybe")
        else:
            print("true")