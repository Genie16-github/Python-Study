# [모의 SW 역량 테스트] 탈주범 검거
from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        for i in pipe[board[x][y]]:
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == 0 and board[nx][ny] != 0:
                for j in pipe[board[nx][ny]]:
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx == x and my == y:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1


dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [2, 1], [2, 3], [0, 3]]

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l_time = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    bfs()

    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 and visited[i][j] <= l_time:
                cnt += 1

    print("#%d %d" % (tc, cnt))
