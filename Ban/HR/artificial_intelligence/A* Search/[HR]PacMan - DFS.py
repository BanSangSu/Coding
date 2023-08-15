'''
    https://www.hackerrank.com/challenges/pacman-dfs
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import copy

sys.stdin = open("data.txt", 'r')

# Score = 0...
def dfs(pacman_r, pacman_c, food_r, food_c, r, c, grid):
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    node_expanded = []
    stack = []
    answer_routes = None
    
    stack.append([pacman_r, pacman_c, []])
    while stack:
        pacman_r, pacman_c, route = stack.pop()
        routes = copy.deepcopy(route)
        routes.append([pacman_r, pacman_c])

        node_expanded.append([pacman_r, pacman_c])
        
        if pacman_r == food_r and pacman_c == food_c:
            if answer_routes == None:
                answer_routes = routes
                break
        
        for direction in directions:
            next_r, next_c = pacman_r + direction[0], pacman_c + direction[1]
            if next_r < 0 or r <= next_r or next_c < 0 or c <= next_c:
                continue
            
            if grid[next_r][next_c] == '-' or grid[next_r][next_c] == '.':
                grid[next_r][next_c] = '='
                stack.append([next_r, next_c, routes])

    print(len(node_expanded))
    for point in node_expanded:
        print(f"{point[0]} {point[1]}")

    print(len(answer_routes)-1)
    for point in answer_routes:
        print(f"{point[0]} {point[1]}")

if __name__ == '__main__':
    pacman_r, pacman_c = map(int, read_line().split())
    food_r, food_c = map(int, read_line().split())
    r, c = map(int, read_line().split())

    grid = [[*map(str, read_line())] for _ in range(r)]

    dfs(pacman_r, pacman_c, food_r, food_c, r, c, grid)