n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)
    W[j].append(i)

visited = [False] * n
prev = [None] * n #prev[u] - это вершина, из которой мы пришли в u
def dfs(start):
    visited[start] = True
    for u in W[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u)
dfs(0)
print(prev)