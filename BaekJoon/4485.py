# [G4]녹색 옷 입은 애가 젤다지?
import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
while True:
    n = int(input().rstrip())
    cnt += 1
    if n == 0:
        break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cave = [[0 for _ in range(n)] for _ in range(n)]
    t_rupee = [[99999 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row = (input().rstrip()).replace(' ', '')
        for j, char in enumerate(row):
            if char != " ":
                cave[i][j] = int(char)

    q = deque()
    q.append((0, 0))
    t_rupee[0][0] = cave[0][0]

    while q:
        i, j = q.popleft()
        visited[0][0] = True

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if t_rupee[nx][ny] > t_rupee[i][j] + cave[nx][ny]:
                        t_rupee[nx][ny] = t_rupee[i][j] + cave[nx][ny]
                        q.append((nx, ny))

    print("Problem {0}: {1}".format(cnt, t_rupee[n - 1][n - 1]))