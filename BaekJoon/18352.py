# [S2]특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
res = []
visited = [-1] * (n+1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        n_node = queue.popleft()
        for i in graph[n_node]:
            if visited[i] == -1:
                visited[i] = visited[n_node] + 1
                queue.append(i)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)

for i in range(n+1):
    if visited[i] == k:
        res.append(i)

if not res:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)