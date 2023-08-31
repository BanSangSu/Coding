'''
    https://www.acmicpc.net/problem/1339
    
'''
import sys

def input_line(): return sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(input_line())
words = [input_line() for _ in range(N)]

alphabet_dict = {}

for word in words:
    power = len(word) - 1
    
    for w in word:
        if w in alphabet_dict:
            alphabet_dict[w] += pow(10, power)
        else:
            alphabet_dict[w] = pow(10, power)
        power -= 1

alphabet_list = sorted(alphabet_dict.values())[::-1]

answer, num = 0, 9

for alphabet in alphabet_list:
    answer += alphabet * num
    num -= 1

print(answer)