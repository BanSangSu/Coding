'''
    https://www.acmicpc.net/problem/1275
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

if __name__ == "__main__":
    N, Q = map(int, read_line().split())
    tree = [0] * (2 * N)

    tree[N:] = map(int, read_line().split())
    for i in range(N - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i + 1]

    for _ in range(Q):
        x, y, a, b = map(int, read_line().split())
        left, right = sorted([x, y])
        left += N - 1
        right += N - 1

        value = 0
        while left <= right:
            if left % 2:
                value += tree[left]
                left += 1

            if not right % 2:
                value += tree[right]
                right -= 1

            left //= 2
            right //= 2
        print(value)

        a += N - 1
        tree[a] = b
        a //= 2

        while a:
            tree[a] = tree[a*2] + tree[a*2 + 1]
            a //= 2
