'''
    https://www.acmicpc.net/problem/1626
'''

import sys; read_line = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open("data.txt", 'r')

def find(a, representative_node):
    if a != representative_node[a]:
        representative_node[a] = find(representative_node[a], representative_node)
    return representative_node[a]

def union(a, b, representative_node):
    a, b = sorted([find(a, representative_node),find(b, representative_node)])
    if a == b:
        return False
    else:
        representative_node[b] = a
        return True


def main():
    V, E = map(int, read_line().split())
    representative_node  = list(range(V+1)) # Representative node
    edges = [tuple(map(int, read_line().split())) for _ in range(E)] # edge list
    sorted_edges = sorted(edges, key=lambda x: x[2])

    start = 0
    cnt = 0
    adj = [ [] for _ in range(V+1)]
    used = set()
    for a, b, w in sorted_edges:
        if union(a, b, representative_node):
            adj[a].append((b, w))
            adj[b].append((a, w))
            start += w
            cnt += 1
            used.add((a, b, w))

    if cnt == V - 1:
        parent = [0] * (V+1)
        dist = [0] * (V+1) # distance to parent
        dist2 = [-1] * (V+1) # second longest distance
        depth = [0] * (V+1)
        depth[1] = 1

        stack = [1]
        while stack:
            cur = stack.pop()
            next_depth = depth[cur]+1
            for next, d in adj[cur]:
                if depth[next]:
                    continue
                parent[next] = cur
                dist[next] = d
                depth[next] = next_depth
                stack.append(next)

        max_depth = max(depth).bit_length()-1

        result = 1<<31
        parent = [parent]
        dist = [dist]
        dist2 = [dist2]
        for i in range(max_depth):
            parent_cnt = [0]*(V+1)
            dist_cnt = [0]*(V+1)
            dist2_cnt = [0]*(V+1)
            for j in range(2, V+1):
                my_parent = parent[-1][j]
                parent_cnt[j] = parent[-1][my_parent]
                dist_cnt[j] = max(dist[-1][j], dist[-1][my_parent])
                temp = sorted({dist[-1][j], dist[-1][my_parent], dist2[-1][j], dist2[-1][my_parent]})
                
                if len(temp) > 1:
                    dist2_cnt[j] = temp[-2]
            parent.append(parent_cnt)
            dist.append(dist_cnt)
            dist2.append(dist2_cnt)

        for a, b, w in edges:
            if (a, b, w) in used:
                continue
            if depth[a] > depth[b]:
                a, b = b, a

            diff = set()
            depth_diff = depth[b] - depth[a]
            for i in range(depth_diff.bit_length()):
                if depth_diff&(1<<i):
                    diff.add(dist[i][b])
                    diff.add(dist2[i][b])
                    b = parent[i][b]

            diff = set(sorted(diff)[-2:])
            for i in range(max_depth, -1, -1):
                next_a, next_b = parent[i][a], parent[i][b]
                if next_a != next_b:
                    diff.add(dist[i][a])
                    diff.add(dist[i][b])
                    diff.add(dist2[i][a])
                    diff.add(dist2[i][b])
                    a, b = next_a, next_b

            if a != b:
                diff.add(dist[0][a])
                diff.add(dist[0][b])
                diff.add(dist2[0][a])
                diff.add(dist2[0][b])
            if len(diff) == 1:
                diff.append(-1)
            diff = sorted(diff)[-2:]

            
            if w > diff[-1]:
                result = min(result, start+w-diff[-1])
            elif w > diff[-2] > -1:
                result = min(result, start+w-diff[-2])

                
        if result == 1 << 31:
            print(-1)
        else:
            print(result)
 
    else:
        print(-1)



if __name__ == "__main__":
    main()
