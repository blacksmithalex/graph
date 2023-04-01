n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)

visited = [False] * n
ans = []
def dfs(start):
    visited[start] = True
    for u in W[start]:
        if not visited[u]:
            dfs(u)
    ans.append(start + 1)

for i in range(n):
    if not visited[i]:
        dfs(i)
ans = [0] + ans[::-1]
print(ans)
