n, m = [int(x) for x in input().split()]
W = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    W[i].append(j)

start = 0
nums = [0] * n
nums[start] = 1
queue = [start]
while queue:
    u = queue.pop()
    for v in W[u]:
        nums[v] += 1
        queue = [v] + queue
print(nums)




