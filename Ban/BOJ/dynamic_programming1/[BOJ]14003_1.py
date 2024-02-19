'''
    https://www.acmicpc.net/problem/14003

    Longest Increasing Subsequence (LIS)
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

sys.stdin = open("data.txt", 'r')

A = int(read_line())
sequence = list(map(int, read_line().split()))