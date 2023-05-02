'''
    https://www.acmicpc.net/problem/1339
    
'''
import sys

def input_line(): return sys.stdin.readline().rstrip()

N = int(input_line())

words = []
for _ in range(N):
    words.append(input_line())

alphabet_dict = {}

for word in words:
    power = len(word) - 1
    
    for c in word:
        if c in alphabet_dict:
            alphabet_dict[c] += pow(10, power)
        else:
            alphabet_dict[c] = pow(10, power)
        power -= 1

alphabet_list = sorted(alphabet_dict.values(), reverse=True)

result, num = 0, 9

for alphabet in alphabet_list:
    result += alphabet * num
    num -=1

print(result)