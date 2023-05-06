'''
    https://www.acmicpc.net/problem/2748

    Dynamic programming
'''
import sys

class fibonacci():
    def __init__(self, n):
        self.n = n + 1
        self.fibo_array = [0] * self.n

    def fibo(self):
        for i in range(self.n):
            if i == 0:
                self.fibo_array[i] = 0
            elif i == 1:
                self.fibo_array[i] = 1
            else:
                self.fibo_array[i] = self.fibo_array[i-1] + self.fibo_array[i-2]

        return self.fibo_array[-1]
    
    def calc(self):
        print(self.fibo())

n = int(sys.stdin.readline())

f = fibonacci(n)

f.calc()