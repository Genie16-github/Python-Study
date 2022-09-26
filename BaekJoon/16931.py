# [S2]겉넓이 구하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

up = n * m

left = 0
for i in range(n):
    for j in range(m):
        if j == 0:
            left += data[i][j]
        else:
            if data[i][j - 1] < data[i][j]:
                left += data[i][j] - data[i][j - 1]

front = 0
for j in range(m):
    for i in range(n):
        if i == 0:
            front += data[i][j]
        else:
            if data[i - 1][j] < data[i][j]:
                front += data[i][j] - data[i - 1][j]

answer = 2 * (up + left + front)
print(answer)