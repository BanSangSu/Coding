'''
    https://www.acmicpc.net/problem/1759
'''
import sys
from itertools import combinations
def input_line(): return sys.stdin.readline().rstrip()

sys.stdin  = open("data.txt", 'r')

L, C = map(int, input_line().split())
words = input_line().split()
words = sorted(words)
vowels = set(['a','e','i','o','u'])

for word in combinations(words, L):
    cnt_vowel = 0
    for w in word:
        if w in vowels:
            cnt_vowel += 1

    if cnt_vowel >= 1 and L - cnt_vowel >= 2: 
        print(("").join(word))