# [S1]효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
res = [0] * (n+1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        n_node = queue.popleft()
        for i in A[n_node]:
            if not visited[i]:
                visited[i] = True
                res[i] += 1
                queue.append(i)


for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i)

maxVal = 0
for i in range(1, n+1):
    maxVal = max(maxVal, res[i])

for i in range(1, n+1):
    if maxVal == res[i]:
        print(i, end=' ')
