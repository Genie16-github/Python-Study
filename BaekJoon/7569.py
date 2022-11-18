# [G5]토마토
from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        for dirt in range(6):
            nx = x + dx[dirt]
            ny = y + dy[dirt]
            if (0 <= nx < m*h) and (0 <= ny < n) and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                graph[nx][ny] = 1
                q.append((nx, ny))


n, m, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m*h)]
visited = [[-1]*n for _ in range(m*h)]

dx = [-1, 0, 1, 0, -m*(h-1), m*(h-1)]
dy = [0, 1, 0, -1, 0, 0]

res = -2147000000
flag = True
q = deque()
for i in range(n):
    for j in range(m*h):
        if graph[j][i] == 1:
            q.append((j, i))
            visited[j][i] = 0

bfs()
for i in range(n):
    for j in range(m*h):
        if graph[j][i] == 0:
            flag = False

if flag:
    for i in range(n):
        for j in range(m*h):
            if visited[j][i] > res:
                res = visited[j][i]
    print(res)
else:
    print(-1)

