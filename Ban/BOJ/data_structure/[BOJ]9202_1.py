'''
    https://www.acmicpc.net/problem/9202
'''
import sys; input_line = lambda: sys.stdin.readline().rstrip()
import collections

# sys.stdin = open("data.txt", 'r')

# Code that passed the test in Python.
class Node(object):
    def __init__(self, char, data=None) -> None:
        self.char = char
        self.data = data
        self.children = {}
        self.found = False

class Trie(object):
    def __init__(self) -> None:
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        if (curr_node.found) or curr_node.data == None:
            return False
        else:
            curr_node.found = True
            return True
        
    def prefix(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True
    
    def initialise(self):
        queue = collections.deque(self.head.children.values())
        while queue:
            curr_node = queue.popleft()
            if curr_node.data != None:
                curr_node.found = False
            queue.extend(curr_node.children.values())


move_r = [0, 0, 1, -1, 1, -1, 1, -1]
move_c = [1, -1, 0, 0, 1, -1, -1, 1]
score_dict = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
board_size = 4

def dfs(trie, row, col, word, checked, count, node):
    if trie.search(word):
        global score
        global total
        global max_word
        score += score_dict[count]
        total += 1
        if count > len(max_word):
            max_word = word
        elif count == len(max_word) and word < max_word:
            max_word = word

    if count == board_size*2:
        return
    
    for move in range(len(move_r)):
        next_row = row + move_r[move]
        next_col = col + move_c[move]
        if (0 <= next_row < board_size and 0 <= next_col < board_size and not checked[next_row][next_col]):
            checked[next_row][next_col] = True
            if board[next_row][next_col] in node.children:
                dfs(trie, next_row, next_col, word+board[next_row][next_col], checked, count+1, node.children[board[next_row][next_col]])
            checked[next_row][next_col] = False


W = int(input_line())
trie = Trie()
for _ in range(W):
    trie.insert(input_line())
input_line()

N = int(input_line())
for t in range(N):
    board = [input_line() for _ in range(board_size)]
    checked = [[False for _ in range(board_size)] for _ in range(board_size)]

    total = 0
    score = 0
    max_word = ''
    trie.initialise()
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] in trie.head.children:
                checked[i][j] = True
                dfs(trie, i, j, board[i][j], checked, 1, trie.head.children[board[i][j]])
                checked[i][j] = False
    print(score, max_word, total)
    if t < N-1:
        input_line()
