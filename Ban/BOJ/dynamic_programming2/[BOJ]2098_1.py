'''
    https://www.acmicpc.net/problem/2098
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def tsp(N, W):
    INF = sys.maxsize
    VISITED_ALL = (1 << N) - 1
    cache = [[None for _ in range(1 << N)] for _ in range(N)]
    
    def find_path(last, visited):
        if visited == VISITED_ALL:
            return W[last][0] or INF
        
        if cache[last][visited] is not None:
            return cache[last][visited]
    
        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and W[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
        cache[last][visited] = tmp
        return tmp
    
    return find_path(0, 1)


N = int(read_line())
W = [[*map(int ,read_line().split())] for _ in range(N)]

print(tsp(N, W))