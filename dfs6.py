n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)
    W[j].append(i)

ret, enter = [0] * n, [0] * n
visited = [False] * n
timer = 0
bridges = []

def dfs(v, p = -1):
    global timer
    visited[v] = True
    enter[v] = timer
    ret[v] = timer
    timer += 1
    for u in W[v]:
        if u == p:
            continue
        if visited[u]:
            ret[v] = min(ret[v], enter[u]);
        else:
            dfs(u, v)
            ret[v] = min(ret[v], ret[u]);
            if ret[u] > enter[v]:
                bridges.append((v + 1, u + 1))

dfs(0)
print(bridges)