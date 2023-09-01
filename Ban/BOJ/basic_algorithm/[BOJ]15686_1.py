'''
    https://www.acmicpc.net/problem/15686

'''

import sys, itertools
def input_line(): return sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

BLANK = 0
HOUSE = 1
CHICKEN = 2

def distance(a: tuple, b: tuple):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def find_chicken(city, N, M):
    houses = []
    chickens = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == HOUSE:
                houses.append((i, j))
            elif city[i][j] == CHICKEN:
                chickens.append((i, j))

    ret = sys.maxsize
    for combs in itertools.combinations(chickens, M):
        comb_dist = 0
        for house in houses:
            chicken_dist = sys.maxsize
            for comb in combs:
                chicken_dist = min(chicken_dist, distance(comb, house))
            comb_dist += chicken_dist
        ret = min(ret, comb_dist)

    return ret
            
            
N, M = map(int, input_line().split())

city = [ list(map(int,input_line().split())) for _ in range(N) ]

print(find_chicken(city, N, M))