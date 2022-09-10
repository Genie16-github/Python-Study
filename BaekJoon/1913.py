# [S3]달팽이
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
data = [[0] * n for _ in range(n)]

dy = [0, 1, 0, -1]  # 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
d = 0
now_x = 0
now_y = 0
now_num = n*n
find_x, find_y = 0, 0

while now_num > 0:
    data[now_x][now_y] = now_num
    if n <= now_x + dx[d] < 0 or n <= now_y + dy[d] < 0 or data[now_x+dx[d]][now_y + dy[d]] != 0:
        d = (d + 1) % 4
    now_y = now_y + dy[d]
    now_x = now_x + dx[d]
    now_num = now_num - 1

for i in range(n):
    for j in range(n):
        if data[i][j] == t:
            find_x = j
            find_y = i
        print(data[i][j], end=' ')
    print()

print(find_y + 1, find_x + 1)

