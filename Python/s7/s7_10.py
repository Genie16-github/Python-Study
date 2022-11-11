# 미로 탐색
import sys
input = sys.stdin.readline


def dfs(x, y):
    global cnt
    if x == y == 6:
        if graph[x][y] == 2:
            cnt += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <= 6) and (0 <= ny <= 6) and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dfs(nx, ny)
                graph[nx][ny] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(7)]
# ch = [[0]*7 for _ in range(7)]
cnt = 0
graph[0][0] = 1
dfs(0, 0)
print(cnt)