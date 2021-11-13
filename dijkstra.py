file = open('test.txt')
N = int(file.readline())
W = [[int(x) for x in file.readline().split()] for i in range(N)] #матрица весов
start, end = [int(x) for x in file.readline().split()]
file.close()

INF = 1e16
visited = [False] * N
dist = [INF] * N
dist[start] = 0

def gofrom():
    index = 0
    distmin = INF
    for i in range(len(visited)):
        if dist[i] < distmin and visited[i] == False:
            distmin = dist[i]
            index = i
    return index

while False in visited:
    u = gofrom()
    for v in range(N):
        if W[u][v] != 0 and (not visited[v]):
            dist[v] = min(dist[u] + W[u][v], dist[v])
    visited[u] = True

print(dist)



