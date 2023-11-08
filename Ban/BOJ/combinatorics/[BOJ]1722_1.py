'''
    https://www.acmicpc.net/problem/1722
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

N = int(read_line())
K = list(map(int, read_line().split()))

cache = {}

def find_permutation(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * find_permutation(n-1)
        return cache[n]

if K[0] == 1:
    k = K[1]
    arrs = [x for x in range(1, N+1)]
    ans = []

    for i in range(N):
        x = find_permutation(N-1-i)
        step = (k-1) // x
        ans.append(arrs[step])
        arrs.remove(arrs[step])
        k -= x * step

    print(*ans)

else:
    input_perm = K[1:]
    sorted_perm = sorted(input_perm)
    ans = 1
    for i in range(N):
        step = sorted_perm.index(input_perm[i])
        sorted_perm.remove(input_perm[i])
        x = find_permutation(N-1-i)
        ans += x * step

    print(ans)
    