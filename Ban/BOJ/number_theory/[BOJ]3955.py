'''
    https://www.acmicpc.net/problem/3955

    Extended Euclidean Algorithm
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def extended_euclidean(a, b, K):
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while r1 != 0:
        q = r0 // r1
        # Calc gcd
        r = r0 % r1
        r0 = r1
        r1 = r

        # Calc s
        s = s0 - q*s1
        s0 = s1
        s1 = s

        # Calc t
        t = t0 - q*t1
        t0 = t1
        t1 = t
    t0 = (t0 % K + K) % K
    if r0 != 1 or t0 > 10**9:
        return "IMPOSSIBLE"
    return t0
    

T = int(read_line())
for i in range(T):
    K, C = map(int, read_line().split())

    if C == 1:
        if K+1 > 10**9:
            print("IMPOSSIBLE")
        else:
            print(K+1)
        continue
    if K == 1:
        print(1)
        continue
    answer = extended_euclidean(K, C, K)
    print(answer)

# # Time out!!
# for i in range(T):
#     member_num, candy_num = map(int, read_line().split())

#     for bunch in range(1, int(10e9 + 1)):
#         read_candy_num = (bunch * candy_num) - 1
#         if read_candy_num % member_num == 0:
#             print(bunch)
#             break

#         if member_num < bunch:
#             print("IMPOSSSIBLE")
#             break