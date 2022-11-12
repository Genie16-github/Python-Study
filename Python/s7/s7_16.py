# 사다리 타기
import sys
input = sys.stdin.readline


def dfs(x, y):
    if x == 0:
        print(y)
        sys.exit(0)
    else:
        for dirt in range(3):
            nx = x + dx[dirt]
            ny = y + dy[dirt]
            if (0 <= nx < 10) and (0 <= ny < 10) and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)
                visited[nx][ny] = 0


dx = [0, 0, -1]
dy = [1, -1, 0]

graph = [list(map(int, input().split())) for _ in range(10)]
s_y = 0
for i in range(10):
    if graph[9][i] == 2:
        s_y = i
visited = [[0]*10 for _ in range(10)]
visited[9][s_y] = 1
dfs(9, s_y)
