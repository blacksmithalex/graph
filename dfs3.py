n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]

for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)
    W[j].append(i)

color = [0] * n
isBipartite = True
def dfs(start):
    for u in W[start]:
        if color[u] == 0:
            color[u] = 3 - color[start]
            dfs(u)
        elif color[u] == color[start]:
            global isBipartite
            isBipartite = False

for i in range(n):
    if color[i] == 0:
        color[i] = 1
        dfs(i)
print(isBipartite)