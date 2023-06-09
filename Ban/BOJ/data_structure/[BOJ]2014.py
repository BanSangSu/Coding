'''
    https://www.acmicpc.net/problem/2014

    Priority Queue
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

sys.stdin = open("data.txt", "r")

if __name__ == "__main__":
        
    # All number is 541 or less
    K, N = map(int, read_line().split())
    prime_nums = list(map(int, read_line().split()))

    priority_queue = []
    for num in prime_nums:
        heapq.heappush(priority_queue, num)

    for i in range(N):
        num = heapq.heappop(priority_queue)
        for j in range(K):
            new_num = num * prime_nums[j]
            heapq.heappush(priority_queue, new_num)

            if num % prime_nums[j] == 0:
                break
    else:
        print(num)