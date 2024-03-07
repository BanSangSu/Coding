'''
    https://www.acmicpc.net/problem/7579

    Knapsack problem (Dynamic programming)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

sys.stdin = open("data.txt", 'r')

N, M = map(int, read_line().split())
memories = [0] + list(map(int, read_line().split()))