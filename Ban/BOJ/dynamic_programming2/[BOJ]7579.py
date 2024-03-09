'''
    https://www.acmicpc.net/problem/7579

    Knapsack problem (Dynamic programming)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

# This code was changed to fail...
N, M = map(int, read_line().split())
memories = [0] + list(map(int, read_line().split()))
deactivate_costs = [0] + list(map(int, read_line().split()))
dp = [[0 for _ in range(sum(deactivate_costs)+1)] for _ in range(N+1)] # For knapsack. idx = costs summation, 
result = sum(deactivate_costs)

for i in range(1, N+1):
    byte = memories[i]
    cost = deactivate_costs[i]

    for j in range(1, sum(deactivate_costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)

print(result) if M != 0 else print(0)