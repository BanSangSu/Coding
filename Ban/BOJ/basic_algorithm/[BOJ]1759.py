'''
    https://www.acmicpc.net/problem/1759

    Brute force
    Combinatorics
    Backtracking

'''
import sys
from itertools import combinations
def input_line(): return sys.stdin.readline()

class problem:
    def __init__(self, l, c, chars) -> None:
        self.l, self.c = l ,c 
        self.chars = sorted(chars)

        self.vowels = set(['a','e','i','o','u'])
        self.words = combinations(self.chars, self.l)

    def solve(self):
        for word in self.words:
            cnt_vow = 0
            for w in word:
                if w in self.vowels:
                    cnt_vow +=1
        
            if cnt_vow >= 1 and self.l - cnt_vow >=2:
                print(''.join(word))
        


l ,c = map(int, input_line().split())
chars = input_line().split()

problem = problem(l ,c ,chars)

problem.solve()