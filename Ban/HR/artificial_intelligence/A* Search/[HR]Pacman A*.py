'''
    https://www.hackerrank.com/challenges/pacman-astar
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

import copy
from collections import deque

# sys.stdin = open("data.txt", 'r')

# 0 score code....
def distance(a, b, x, y):
    return abs(a - x) + abs(b - y)

def a_star(pacman_r, pacman_c, food_r, food_c, r, c, grid):
    directions = [(-1,0), (0,-1), (0,1), (1, 0)]
    answer_route = None
    dq = deque()

    dq.append([pacman_r, pacman_c, []])
    while dq:
        x, y, route = dq.popleft()
        routes = copy.deepcopy(route)
        routes.append([x,y])

        if x == food_r and y == food_c:
            if answer_route == None:
                answer_route = routes
                break
        
        possible_moves = []
        for direction in directions:
            next_r, next_c = x + direction[0], y + direction[1]
            if next_r < 0 or r <= next_r or next_c < 0 or c <= next_c:
                continue

            if grid[next_r][next_c] == '.' or grid[next_r][next_c] == '-':
                grid[next_r][next_c] = '='
                possible_moves.append([next_r, next_c, distance(food_r, food_c, next_r, next_c)])
        
        possible_moves.sort(key = lambda x: x[2])
        for move in possible_moves:
            dq.append([move[0], move[1], routes])

    print(len(answer_route)-1)
    for point in answer_route:
        print(f"{point[0]} {point[1]}")


if __name__ == "__main__":
    pacman_r, pacman_c = map(int, read_line().split())
    food_r, food_c = map(int, read_line().split())
    r, c = map(int, read_line().split())
    grid = [[*map(str, read_line())] for _ in range(r)]

    a_star(pacman_r, pacman_c, food_r, food_c, r, c, grid)
