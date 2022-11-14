# [D4]파핑파핑 지뢰찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def check2(x, y):
    for dirt in range(8):
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        if (0 <= nx < n) and (0 <= ny < n) and ch[nx][ny] != -1:
            ch[nx][ny] = -1


def check(x, y):
    for dirt in range(8):
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == '.':
            ch[nx][ny] += 1


dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '*':
                ch[i][j] = -1
                check(i, j)
    cnt = 0
    for x in ch:
        print(x)
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                ch[i][j] = -1
                check2(i, j)
                cnt += 1

    for i in range(n):
        for j in range(n):
            if ch[i][j] != -1:
                ch[i][j] = -1
                cnt += 1

    print("#%d %d" % (tc, cnt))


