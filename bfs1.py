n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)
    W[j].append(i)

start = 0
dist = [-1] * n
dist[start] = 0
queue = [start]
while queue:
    u = queue.pop()
    for v in W[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue = [v] + queue
print(dist)





