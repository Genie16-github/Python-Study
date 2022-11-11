# 등산경로
import sys
input = sys.stdin.readline


def dfs(x, y):
    global cnt
    if x == e_x and y == e_y:
        cnt += 1
        return
    else:
        for dirt in range(4):
            nx = x + dx[dirt]
            ny = y + dy[dirt]
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] > graph[x][y] and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                dfs(nx, ny)
                ch[nx][ny] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
min_xy = 2147000000
max_xy = -214700000
s_x = s_y = 0
e_x = e_y = 14
for i in range(n):
    for j in range(n):
        if graph[i][j] < min_xy:
            min_xy = graph[i][j]
            s_x = i
            s_y = j
        if graph[i][j] > max_xy:
            max_xy = graph[i][j]
            e_x = i
            e_y = j
ch[s_x][s_y] = 1
cnt = 0
dfs(s_x, s_y)
print(cnt)