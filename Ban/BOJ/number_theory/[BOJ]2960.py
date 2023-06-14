'''
    https://www.acmicpc.net/problem/2960
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

# Tidy
N, K = map(int, read_line().split())

num_chk = [False] * (N+1)
cnt = K
flag = False
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if num_chk[j] == False:
            num_chk[j] = True
            cnt -= 1
            if cnt == 0:
                print(j)
                flag = True
                break
    if flag:
        break

# # Before

# num_chk = [False] * (N+1)
# cnt = K
# for i in range(2, N+1):
#     for j in range(1, N+1):
#         t =  i*j
#         if t > N:
#             break
#         if num_chk[t] == True:
#             continue
#         num_chk[t] = True
#         cnt -= 1

#         if cnt <= 0:
#             print(t)
#             break
#     if cnt <= 0:
#         break


