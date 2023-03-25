n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)

color = [0] * n
CycleFound = False
def dfs(start):
    color[start] = 1
    for u in W[start]:
        if color[u] == 0:
            dfs(u)
        elif color[u] == 1:
            global CycleFound
            CycleFound = True
    color[start] = 2

for i in range(n):
    if color[i] == 0:
        dfs(i)
print(CycleFound)