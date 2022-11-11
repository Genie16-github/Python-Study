# 단지 번호 붙이기
import sys
input = sys.stdin.readline


def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for dirt in range(4):
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 1:
            dfs(nx, ny)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if graph[i][j] == 1:
            dfs(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for x in res:
    print(x)