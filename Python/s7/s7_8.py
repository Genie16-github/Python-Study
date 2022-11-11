# 사과나무
from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    global cnt
    while q:
        if v == s:
            break
        size = len(q)
        for i in range(size):
            tmp = q.popleft()
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if ch[x][y] == 0:
                    cnt += graph[x][y]
                    ch[x][y] = 1
                    q.append((x, y))
        v += 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
q = deque()
s = n // 2
q.append((s, s))
cnt = 0
ch[s][s] = 1
cnt += graph[s][s]
bfs(0)
print(cnt)

