# 토마토
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
date = [[0]*n for _ in range(m)]
q = deque()
res = -2147000000
tf = True

for i in range(n):
    for j in range(m):
        if graph[j][i] == 1:
            q.append((j, i))
# print(q)

while q:
    p = q.popleft()
    for i in range(4):
        x = p[0] + dx[i]
        y = p[1] + dy[i]
        if (0 <= x < m) and (0 <= y < n) and graph[x][y] == 0:
            q.append((x, y))
            graph[x][y] = 1
            date[x][y] = date[p[0]][p[1]] + 1

for i in range(n):
    for j in range(m):
        if graph[j][i] == 0:
            tf = False


for i in range(n):
    for j in range(m):
        if date[j][i] > res:
            res = date[j][i]

if res == 0 and tf:
    print(0)
elif not tf:
    print(-1)
else:
    print(res)

