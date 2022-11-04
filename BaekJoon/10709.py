# [S5]기상캐스터
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [input() for _ in range(H)]
cloud = False
res = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if board[i][j] == 'c':
            cloud = True
            res[i][j] = 0
            continue

        if cloud:
            res[i][j] = res[i][j-1] + 1

    cloud = False

for i in range(H):
    print(*res[i])



