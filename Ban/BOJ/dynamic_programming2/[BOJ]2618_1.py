'''
    https://www.acmicpc.net/problem/2618
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize

N = int(read_line())
W = int(read_line())

case_locations = [(N,N), (1,1)]
case_locations.extend([tuple(map(int, read_line().split())) for _ in range(W)])

dp = [[INF for _ in range(W+1)] for _ in range(W+1)]
dp[0][0] = 0
for x in range(2, W+2):
    i, j = case_locations[x]
    previous_i, previous_j = case_locations[x-1]
    for y in range(x):
        rest_i, rest_j = case_locations[y]
        dp[x-1][y] = min(dp[x-1][y], dp[x-2][y] + abs(i-previous_i) + abs(j-previous_j))
        dp[x-1][x-1] = min(dp[x-1][x-1], dp[x-2][y] + abs(i-rest_i) + abs(j-rest_j))

print(min(dp[-1]))


def dp_find(police_car_location, depth):
    if depth == W:
        return police_car_location
    
    i, j = case_locations[W+1-depth]
    if police_car_location == W-depth:
        for x in range(W-depth):
            last_i, last_j = case_locations[x]
            if dp[W-depth][police_car_location] - dp[W-1-depth][x] == abs(i-last_i) + abs(j-last_j):
                ans = dp_find(x, depth+1)
                print((ans+1) % 2 + 1)
                return (ans+1) % 2
    else:
        last_i, last_j = case_locations[W-depth]
        if dp[W-depth][police_car_location] - dp[W-1-depth][police_car_location] == abs(i-last_i) + abs(j-last_j):
            ans = dp_find(police_car_location, depth+1)
            print(ans % 2 + 1)
            return ans


dp_find(dp[-1].index(min(dp[-1])), 0)