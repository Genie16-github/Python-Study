# [모의 SW 역량테스트] 홈 방범 서비스
from collections import deque


def bfs(x, y, k):
    global cnt
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    q = deque([(x, y)])

    home = board[x][y]
    if home * m - (k*k + (k-1)*(k-1)) >= 0:
        cnt = max(home, cnt)
    while k < n+2:
        for _ in range(len(q)):
            a, b = q.popleft()
            for dirt in range(4):
                na = a + dx[dirt]
                nb = b + dy[dirt]
                if (0 <= na < n) and (0 <= nb < n) and visited[na][nb] == 0:
                    visited[na][nb] = 1
                    q.append((na, nb))
                    if board[na][nb] == 1:
                        home += 1
        k += 1
        if home * m - (k*k + (k-1)*(k-1)) >= 0:
            cnt = max(home, cnt)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())  # n : 도시 크기, m : 하나의 집이 지불할 수 있는 비용
    board = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j, 1)
    print("#%d %d" % (tc, cnt))
