'''
    https://www.acmicpc.net/problem/15686

'''

import sys, itertools
def input_line(): return sys.stdin.readline().rstrip()
BLANK = 0
HOUSE = 1
CHICKEN = 2

def distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
    

def find_chicken(city, N, M):
    chickens = []
    houses = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == CHICKEN:
                chickens.append((i,j))
            elif city[i][j] == HOUSE:
                houses.append((i,j))
    
    result = sys.maxsize

    chicken_combs = list(itertools.combinations(chickens, M))
    for chicken_comb in chicken_combs:
        city_dist = 0
        for house in houses:
            min_distance = min([distance(chicken, house) for chicken in chicken_comb])
            city_dist += min_distance
        if city_dist < result:
            result = city_dist

    return result

N, M = map(int, input_line().split())

city = [ list(map(int,input_line().split())) for _ in range(N) ]

print(find_chicken(city, N, M))