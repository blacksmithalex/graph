n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)
    W[j].append(i)

visited = [False] * n
def dfs(start):
    visited[start] = True
    for u in W[start]:
        if not visited[u]:
            dfs(u)

ncomp = 0
for i in range(n):
    if not visited[i]:
        ncomp += 1
        dfs(i)
print(ncomp)