'''
    https://www.acmicpc.net/problem/2014
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()
import heapq

# sys.stdin = open("data.txt", "r")

if __name__ == "__main__":
        
    K, N = map(int, read_line().split())
    prime_nums = list(map(int, read_line().split()))
    priority_queue = list(prime_nums) 
    heapq.heapify(priority_queue)

    head = None
    for _ in range(N):
        head = heapq.heappop(priority_queue)
        for prime in prime_nums:
            heapq.heappush(priority_queue, prime * head)
            if head % prime == 0:
                break

    print(head)