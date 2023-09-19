'''
    https://www.acmicpc.net/problem/6416
'''
import sys; input_readline = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

cases, case = [], []
while True:
    temp = [*map(int, input_readline().split())]
    if temp:
        if temp[-1] == -1 and temp[-2] == -1:
            break
        elif temp[-1] == 0 and temp[-2] == 0:
            case.extend(temp[:-2])
            cases.append(case)
            case = []
        else:
            case.extend(temp)

for k, case in enumerate(cases):
    nodes, indegrees, edge_cnt = set(), set(), 0
    flag = True
    for i in range(0, len(case), 2):
        u, v = case[i], case[i+1]
        if v in indegrees:
            flag = False
            break

        edge_cnt += 1
        nodes.add(u)
        nodes.add(v)
        indegrees.add(v)

    if edge_cnt > 0 and len(nodes) != edge_cnt+1:
        flag = False
    if flag:
        print('Case {} is a tree.'.format(k+1))
    else:
        print('Case {} is not a tree.'.format(k+1))