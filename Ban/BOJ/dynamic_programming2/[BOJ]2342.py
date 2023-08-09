'''
    https://www.acmicpc.net/problem/2342
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

INF = sys.maxsize
movements = list(map(int, read_line().split()))
number_of_movement = 5

# dp[Nth move][left_location][right_location]
dp = [[[INF for _ in range(number_of_movement)] for _ in range(number_of_movement)] for _ in range(len(movements))]
dp[0][0][0] = 0

def get_distance(curr, target):
    if curr == target:
        return 1
    elif curr == 0:
        return 2
    elif abs(curr - target) % 2 == 0:
        return 4
    else:
        return 3


for i in range(1, len(movements)):
    move = movements[i-1]
    for left in range(number_of_movement):
        for right in range(number_of_movement):
            dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + get_distance(left, move))
            dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + get_distance(right, move))

result = INF
for i in range(number_of_movement):
    for j in range(number_of_movement):
        result = min(result, dp[len(movements)-1][i][j])
print(result)
