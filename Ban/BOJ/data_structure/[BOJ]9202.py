'''
    https://www.acmicpc.net/problem/9202

    Trie
    DFS
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')
# PyPy can pass the test.
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = dict()
        self.is_end = False

class Boggle:
    def __init__(self, W, num_rows = 4) -> None:
        self.W = W
        self.num_rows = num_rows

        self.word_dict = dict()
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.result = set()

    # Insert words in Trie
    def make_trie(self, temp):
        if temp[0] in self.word_dict:
            pre = self.word_dict[temp[0]]
        else:
            self.word_dict[temp[0]] = Node(temp[0])
            pre = self.word_dict[temp[0]]

        if len(temp) == 1:
            pre.is_end = True
        for i in range(1, len(temp)):
            if temp[i] not in pre.children:
                pre.children[temp[i]] = Node(temp[i])
            pre = pre.children[temp[i]]
            if i == len(temp) - 1:
                pre.is_end = True

    # Input words
    def input_word(self):
        for _ in range(self.W):
            temp = input_line()
            self.make_trie(temp)

    # Create board
    def create_board(self):
        board = []
        for _ in range(self.num_rows):
            board.append(list(input_line()))
        return board

    # Search word using index i, j, DFS
    def search_word(self, board, i, j, visited, word, trie):
        word += board[i][j]
        
        if trie.is_end == True:
            self.result.add(word)
        visited[i][j] = True
        for k in range(len(self.dx)):
            x = i + self.dx[k]
            y = j + self.dy[k]
            if x < 0 or self.num_rows <= x or y < 0 or self.num_rows <= y:
                continue
            if visited[x][y] == True:
                continue
            if board[x][y] in trie.children:
                self.search_word(board, x, y, visited, word, trie.children[board[x][y]])
                visited[x][y] = False

    # return longest word
    def check_longest_word(self):
        temp = sorted(self.result, key = lambda x: (-len(x), x))
        return temp[0]

    # return point
    def check_point(self):
        point = 0
        for i in self.result :
            if len(i) < 3 :
                continue
            elif len(i) < 5 :
                point += 1
            elif len(i) == 5 :
                point += 2
            elif len(i) == 6 :
                point += 3
            elif len(i) == 7 :
                point += 5
            elif len(i) == 8 :
                point += 11
        return point
    
    # Print answer
    def print_answer(self):
        point = str(self.check_point())
        longest_word = self.check_longest_word()
        cnt = str(len(self.result))
        answer = point + " " + longest_word + " " + cnt
        return answer
    
    def do_boggle(self):
        board = self.create_board()
        self.result.clear()
        for i in range(self.num_rows):
            for j in range(self.num_rows):
                visited = [[False for _ in range(self.num_rows)] for _ in range(self.num_rows)]
                if board[i][j] in self.word_dict:
                    trie = self.word_dict[board[i][j]]
                    self.search_word(board, i, j, visited, '', trie)
        print(self.print_answer())

W = int(input_line())
boggle = Boggle(W)
boggle.input_word()
input_line()

B = int(input_line())
boggle.do_boggle()
for _ in range(B-1):
    input_line()
    boggle.do_boggle()
