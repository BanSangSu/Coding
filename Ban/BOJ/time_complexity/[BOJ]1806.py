'''
    https://www.acmicpc.net/problem/1806

    Two pointer
'''
import sys; input_line = sys.stdin.readline

seq_len, sum_min = map(int, input_line().rstrip().split())
array = list(map(int, input_line().rstrip().split()))

start, end = 0, 0
temp_sum = array[0]
ans = seq_len + 1

while start <= end:
    if temp_sum >= sum_min:
        ans = min(ans, end - start + 1)
        temp_sum -= array[start]
        start += 1
    else:
        end += 1
        if end < seq_len:
            temp_sum += array[end]
        else:
            break

if (ans == seq_len+1): ans = 0
print(ans)