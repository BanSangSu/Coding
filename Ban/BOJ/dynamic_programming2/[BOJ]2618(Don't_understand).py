'''
    https://www.acmicpc.net/problem/2618
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
# sys.stdin = open("data.txt", 'r')

# I don't understand what this code means...
def dp_find(police_car_location, depth):
    if depth == W:
        return police_car_location
    i, j = locations[W+1-depth]                     # last case location
    rest_i, rest_j = locations[police_car_location] # rest police cars' location
    if police_car_location == W-depth:              # When the police car location is at the last second
        for x in range(W-depth):
            last_i, last_j = locations[x]
            if dp[W-depth][police_car_location] - dp[W-1-depth][x] == abs(i-last_i) + abs(j-last_j):
                ans = dp_find(x, depth+1)
                print((ans+1) % 2 + 1)
                return (ans+1) % 2
    else:
        last_i, last_j = locations[W-depth]
        if dp[W-depth][police_car_location] - dp[W-1-depth][police_car_location] == abs(i-last_i) + abs(j-last_j):
            ans = dp_find(police_car_location, depth + 1)
            print(ans % 2 + 1)
            return ans

INF = sys.maxsize

N = int(read_line())
W = int(read_line())

# locations[0] = polic car2, locations[1] = polic car1, locations[2~] = cases
locations = [(N,N), (1,1)]
for _ in range(W):
    i,j = map(int, read_line().split())
    locations.append((i,j))

dp = [[INF for _ in range(W+1)] for _ in range(W+1)] # dp[i][x]
dp[0][0] = 0
for x in range(2, W+2):
    i, j = locations[x]                 # now case location
    previous_i, previous_j = locations[x-1]     # previous case location
    for y in range(x):                  # rest case location
        rest_i, rest_j = locations[y]
        dp[x-1][y] = min(dp[x-1][y], dp[x-2][y] + abs(i-previous_i) + abs(j-previous_j))
        dp[x-1][x-1] = min(dp[x-1][x-1], dp[x-2][y] + abs(i-rest_i) + abs(j-rest_j))

print(min(dp[-1]))

dp_find(dp[-1].index(min(dp[-1])), 0)