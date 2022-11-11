# 미로의 최단거리 통로
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [[8] + list(map(int, input().split())) + [8] for _ in range(7)]
graph.insert(0, [8]*9)
graph.append([8]*9)
ch = [[0]*9 for _ in range(9)]
cnt = [[0]*9 for _ in range(9)]
q = deque()
ch[1][1] = 1
q.append((1, 1))

while q:
    size = len(q)
    p = q.popleft()
    if p == (7, 7):
        print(cnt[7][7])
        break
    for i in range(size):
        for j in range(4):
            x = p[0] + dx[j]
            y = p[1] + dy[j]
            if (0 < x < 8) and (0 < y < 8) and graph[x][y] == 0 and ch[x][y] == 0:
                cnt[x][y] = cnt[p[0]][p[1]] + 1
                ch[x][y] = 1
                q.append((x, y))
else:
    print(-1)