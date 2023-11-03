'''
    https://www.acmicpc.net/problem/5568
'''
import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')


result = set()

def backtracking(string, is_cards, cards, depth):
    if depth == K:
        result.add("".join(string))
        return
    
    for i in range(N):
        if is_cards[i]:
            continue
        
        is_cards[i] = True
        string.append(cards[i])
        backtracking(string, is_cards, cards, depth + 1)
        string.pop()
        is_cards[i] = False



N = int(read_line())
K = int(read_line())

cards = [read_line() for _ in range(N)]
is_cards = [ False for _ in range(N)]
backtracking([], is_cards, cards, 0)

print(len(result))