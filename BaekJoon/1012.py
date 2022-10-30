# [S2]유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀의 한도를 풀어주는 함수


def dfs(x, y):
    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1  # x, y 반대로
    # print(matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)
