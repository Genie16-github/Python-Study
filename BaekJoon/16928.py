# [G5]뱀과 사다리 게임
from collections import deque

n, m = map(int, input().split())
move = []
for i in range(n+m):
    move.append(list(map(int, input().split())))

q = deque()
q.append((1, 0))
visited = [False] * 101
visited[1] = True
dx = [1, 2, 3, 4, 5, 6]


def bfs():
    while q:
        x, cnt = q.popleft()
        if x == 100:
            print(cnt)
            return

        for dirt in range(6):
            nx = x + dx[dirt]
            if nx < 101:
                if not visited[nx]:
                    visited[nx] = True
                    nx = check(nx)
                    visited[nx] = True
                    q.append((nx, cnt+1))


def check(x):
    for j in move:
        if x == j[0]:
            x = j[1]
            return x
    return x


bfs()
