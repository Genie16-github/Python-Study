# 섬나라 아일랜드
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))
            while q:
                p = q.popleft()
                for dirt in range(8):
                    x = p[0] + dx[dirt]
                    y = p[1] + dy[dirt]
                    if (0 <= x < n) and (0 <= y < n) and graph[x][y] == 1:
                        graph[x][y] = 0
                        q.append((x, y))
            cnt += 1

print(cnt)