'''
    https://www.acmicpc.net/problem/2580

    Backtracking

    # Timeout. But the main code except for class code is passed.
'''
import sys
def input_line(): return sys.stdin.readline()

class sudoku_problem:

    def __init__(self, N:int, sudoku: list, zeros: list) -> None:
        self.N = N
        self.sudoku = sudoku
        self.zeros = zeros

        self.flag = 0

    def is_promising(self, i, j):
        promising = [x for x in range(1, 10)]

        # Check rows, cols
        for k in range(N):
            if self.sudoku[i][k] in promising:
                promising.remove(self.sudoku[i][k])
            if self.sudoku[k][j] in promising:
                promising.remove(self.sudoku[k][j])

        # Check 3 * 3 box
        i //= 3
        j //= 3
        for p in range(i*3, (i+1)*3):
            for q in range(j*3, (j+1)*3):
                if self.sudoku[p][q] in promising:
                    promising.remove(self.sudoku[p][q])
        
        return promising

    def dfs(self, x):

        if self.flag: # already solved
            return 
        
        if x == len(self.zeros): 
            for row in self.sudoku:
                print(*row)
            self.flag = True
            return
        
        else:
            (i, j) = self.zeros[x]
            promising = self.is_promising(i, j)

            for num in promising:
                self.sudoku[i][j] = num
                self.dfs(x + 1) # next zeros
                sudoku[i][j] = 0
        

    def solve(self):
        self.dfs(0)


N = 9
sudoku = [list(map(int, input_line().split())) for _ in range(N)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

sudoku_problem = sudoku_problem(N, sudoku, zeros)
sudoku_problem.solve()