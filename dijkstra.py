n = int(input())
W = [[int(x) for x in input().split()] for _ in range(n)]
start = int(input()) - 1

INF = 1e8
visited = [False] * n
dist = [INF] * n
dist[start] = 0

def gofrom():
    index = 0
    distmin = INF
    for i in range(n):
        if dist[i] < distmin and visited[i] == False:
            distmin = dist[i]
            index = i
    return index

while False in visited:
    u = gofrom()
    for v in range(n):
        if W[u][v] != 0 and (not visited[v]):
            dist[v] = min(dist[v], dist[u] + W[u][v])
    visited[u] = True

print(dist)
