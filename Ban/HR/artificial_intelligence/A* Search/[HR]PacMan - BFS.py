'''
    https://www.hackerrank.com/challenges/pacman-bfs
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
from collections import deque
import copy

# sys.stdin = open("data.txt", 'r')

# 0 score!?!?!, though I passed the problems!?
def bfs(pacman_r, pacman_c, food_r, food_c, r, c, grid):
    directions = [(-1,0), (0,-1), (0, 1), (1,0)]
    answer_route = None
    node_expanded = []
    dq = deque()

    dq.append([pacman_r, pacman_c, []])
    while dq:
        x, y, route = dq.popleft()
        routes = copy.deepcopy(route)
        routes.append([x, y])
        
        node_expanded.append([x, y])

        if x == food_r and y == food_c:
            if answer_route == None:
                answer_route = routes
                break

        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if next_x < 0 or r <= next_x or next_y < 0 or c <= next_y:
                continue

            if grid[next_x][next_y] == '-' or grid[next_x][next_y] == '.':
                 grid[next_x][next_y] = '='
                 dq.append([next_x, next_y, routes])
    
    print(len(node_expanded))
    for point in node_expanded:
        print(f"{point[0]} {point[1]}")

    print(len(answer_route)-1)
    for point in answer_route:
        print(f"{point[0]} {point[1]}")

if __name__ == "__main__":
    pacman_r, pacman_c = map(int, read_line().split())
    food_r, food_c = map(int, read_line().split())
    r, c = map(int, read_line().split())
    grid = [[*map(str, read_line())] for _ in range(r)]
    bfs(pacman_r, pacman_c, food_r, food_c, r, c, grid)