'''
    https://www.acmicpc.net/problem/4375
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

while True:
    try:
        n = int(read_line())
    except:
        break
    
    num = 0
    i = 1
    while True:
        num = num*10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1
