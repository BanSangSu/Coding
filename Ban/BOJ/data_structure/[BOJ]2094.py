'''
    https://www.acmicpc.net/problem/2094

    Segment Tree
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

# Input 1
N = int(read_line())

data = [tuple(map(int, read_line().split())) for _ in range(N)]

# Segment tree
tree = [0]*(N << 2)

def max_segment(start, end, node):
    if start == end:
        tree[node] = data[start-1][1]
    else:
        mid = (start+end) >> 1
        tree[node] = max(max_segment(start, mid, node << 1), max_segment(mid + 1, end, (node << 1) | 1))
    return tree[node]
max_segment(1, N, 1)

def search(year):
    start = 1
    end = N
    while start < end:
        mid = (start+end) >> 1
        if year > data[mid - 1][0]:
            start = mid + 1
        else:
            end = mid
    if data[start-1][0] == year:
        return data[start-1][1], start
    else:
        return -1, start
    
def query(start, end, node, left, right):
    if end < left or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start+end) >> 1
        return max(query(start, mid, node << 1, left, right), query(mid+1, end, (node << 1) | 1, left, right))

# Input 2
M = int(read_line())

for _ in range(M):
    y, x = map(int, input().split())
    precipitation_y, node_y = search(y)
    precipitation_x, node_x = search(x)
    
    if precipitation_y == -1 and precipitation_x == -1:
        print('maybe')
    elif precipitation_y == -1:
        if query(1, N, 1, node_y, node_x-1) < precipitation_x:
            print('maybe')
        else:
            print('false')
    elif precipitation_x == -1:
        if query(1, N, 1, node_y+1, node_x-1) < precipitation_y:
            print('maybe')
        else:
            print('false')
    else:
        if precipitation_y < precipitation_x or precipitation_x <= query(1, N, 1, node_y+1, node_x-1):
            print('false')
        elif not x-y == node_x-node_y:
            print('maybe')
        else:
            print('true')

# #######
# # Fail.... only pass the test case....
# TRUE = 1
# FALSE = 0
# MAYBE = -1
# MAXN = 50001

# years = [0] * MAXN
# tree = [0] * (MAXN << 2)
# base = 1
# y, x = 0, 0

# def get_index(val) -> int:
#     left, right = 0, N
#     while left < right:
#         mid = (left+right) >> 1
#         if years[mid] < val:
#             left = mid + 1
#         else:
#             right = mid
#     return right

# def get_max(left, right) -> int:
#     ret = 0
#     left += base
#     right += base

#     while left <= right:
#         if (left & 1):
#             ret = max(ret, tree[left])
#             left += 1
#         if (not(right & 1)):
#             ret = max(ret, tree[right])
#             right -= 1
#         left >>= 1
#         right >>= 1
#     return ret

# def judge():
#     x_idx, y_idx = get_index(x), get_index(y)
#     x_chk = 1 if x_idx < N and years[x_idx] else 0
#     y_chk = 1 if y_idx < N and years[y_idx] else 0
  
#     if (x_chk and y_chk and tree[base+y_idx] < tree[base+x_idx]): return FALSE

#     find_x_idx, find_y_idx = x_idx, y_idx
#     while x <= years[find_x_idx]: find_x_idx -= 1
#     while y >= years[find_y_idx]: find_y_idx += 1

#     max_val = get_max(find_y_idx, find_x_idx)
    
#     if (x_chk and tree[base+x_idx] <= max_val): return FALSE
#     if (y_chk and tree[base+y_idx] <= max_val): return FALSE

#     if (x_chk and y_chk and y - x == y_idx - x_idx): return TRUE
    
#     return MAYBE

# if __name__ == "__main__":

#     N = int(read_line())
#     while (base < N): base <<=1
#     years[N] = 1e9

#     for i in range(0, N):
#         # year, precipitation 
#         years[i], tree[base + i]= [*map(int, read_line().split())]

#         idx = (base + i) // 2
#         while idx:
#             tree[idx] = max(tree[(idx << 1)], tree[((idx << 1) | 1)])
#             idx >>= 1

#     M = int(read_line())
#     while 0 < M:
#         M -= 1
#         y, x = [*map(int, read_line().split())]
#         ans = judge()
#         if ans == TRUE:
#             print("true")
#         elif ans == MAYBE:
#             print("maybe")
#         else:
#             print("false")
   