# [s1]안전 영역
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
res = -2147000000

for h in range(100):
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and graph[i][j] > h:
                q.append((i, j))
                ch[i][j] = 1
                while q:
                    p = q.popleft()
                    for dirt in range(4):
                        x = p[0] + dx[dirt]
                        y = p[1] + dy[dirt]
                        if (0 <= x < n) and (0 <= y < n) and graph[x][y] > h and ch[x][y] == 0:
                            ch[x][y] = 1
                            q.append((x, y))
                cnt += 1
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)