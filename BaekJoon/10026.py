# [G5]적록색약
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    visited[x][y] = 1
    for dirt in range(4):
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny]:
                if graph[x][y] == graph[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny)


n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt, end=' ')

cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)