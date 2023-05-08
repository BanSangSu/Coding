'''
    https://www.acmicpc.net/problem/2096

    Dynamic programming(Memoization)
'''
import sys
def input_line(): return sys.stdin.readline().rstrip()

def memoization(N, table, row_size):
    min_dp = table
    max_dp = table
    for i in range(N-1):
        table = list(map(int, input_line().split()))
        # Use Sliding Window Algorithm (https://medium.com/geekculture/implement-a-sliding-window-using-python-31d1481842a7)
        
        # Simple version
        min_dp = [table[0]+min(min_dp[0], min_dp[1]), table[1]+min(min_dp), table[2]+min(min_dp[1], min_dp[2])]
        max_dp = [table[0]+max(max_dp[0], max_dp[1]), table[1]+max(max_dp), table[2]+max(max_dp[1], max_dp[2])]

        # Row size flexable version
        # temp_min_dp = []
        # temp_max_dp = []
        # for j in range(row_size):
        #     if j == 0:
        #         temp_min_dp.append(table[j]+min(min_dp[j], min_dp[j+1]))
        #         temp_max_dp.append(table[j]+max(max_dp[j], max_dp[j+1]))
        #     elif j == row_size-1:
        #         temp_min_dp.append(table[j]+min(min_dp[j-1], min_dp[j]))
        #         temp_max_dp.append(table[j]+max(max_dp[j-1], max_dp[j]))
        #     else:
        #         temp_min_dp.append(table[j]+min(min_dp[j-1], min_dp[j], min_dp[j+1]))
        #         temp_max_dp.append(table[j]+max(max_dp[j-1], max_dp[j], max_dp[j+1]))
        # min_dp = temp_min_dp
        # max_dp = temp_max_dp
    print(max(max_dp), min(min_dp))

N = int(input_line())

# Initialize min, max DP by receiving the first input list
table = list(map(int, input_line().split()))
row_size = 3

memoization(N, table, row_size)