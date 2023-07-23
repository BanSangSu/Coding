'''
    https://www.acmicpc.net/problem/3860

    Bellman-Ford algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# Next -> We have to change this code to SPFA(Shortest Path Faster Algorithm).
# sys.stdin = open("data.txt", 'r')

# tombstone = -1, blank = 0, hole = 1 ~.

# Pypy passed code.
# We have to set INF float('inf') and cycle return float('-inf') if you don't you can't pass the tests. I don't know why.....
INF = float('inf')

def bellman_ford(W, H, graph, hole):
    dist = [[INF for _ in range(H)] for _ in range(W)]
    dist[0][0] = 0

    for count in range(H*W):
        for x in range(W):
            for y in range(H):
                if x == W-1 and y == H-1 or graph[x][y] == -1:
                    continue
                
                elif 1 <= graph[x][y]:
                    outX, outY, outT = hole[graph[x][y]]
                    if dist[x][y] + outT < dist[outX][outY]:
                        dist[outX][outY] = dist[x][y] + outT 
                        
                        if count == H*W-1:  
                            return float('-inf')    
                
                elif graph[x][y] == 0:
                    for nx, ny in ([x, y+1], [x, y-1], [x+1, y], [x-1, y]):
                        if 0 <= nx < W and 0 <= ny < H:
                            if graph[nx][ny] >= 0:
                                if dist[x][y] + 1 < dist[nx][ny]:
                                    dist[nx][ny] = dist[x][y] + 1

                                    if count == H*W-1:
                                        return float('-inf')
    return dist[W-1][H-1]
                

while True:
    W, H = map(int, read_line().split())
    if W == 0 and H == 0:
        break

    G = int(read_line())

    graph = [[0 for _ in range(H)] for _ in range(W)]
    hole = [(INF, INF, INF)]
    for _ in range(G):
        X, Y = map(int, read_line().split())
        graph[X][Y] = -1

    E = int(read_line())
    for i in range(1, E+1):
        X1, Y1, X2, Y2, T = map(int, read_line().split())
        graph[X1][Y1] = i
        hole.append((X2, Y2, T))


    result = bellman_ford(W, H, graph, hole)
    if result == INF:
        print('Impossible')
    elif result == float('-inf'):
        print('Never')
    else:
        print(result)