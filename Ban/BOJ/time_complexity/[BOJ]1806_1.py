'''
    https://www.acmicpc.net/problem/1806
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

seq_len, sum_min = map(int, input_line().split())
sequences = [*map(int, input_line().split())]

left, right = 0, 0
temp_sum = sequences[0]
ans = seq_len + 1
while left <= right:
    if sum_min <= temp_sum:
        temp_len = (right-left+1)
        if temp_len < ans:
            ans = temp_len
        temp_sum -= sequences[left]
        left += 1
    else:
        right+= 1
        if right < seq_len:
            temp_sum += sequences[right]
        else:
            break
        
if (ans == seq_len+1): ans = 0        
print(ans)