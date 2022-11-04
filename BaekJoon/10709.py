# [S5]기상캐스터
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [input() for _ in range(H)]
cloud = False
board2 = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if board[i][j] == 'c':
            cloud = True
            board2[i][j] = 0
            continue

        if cloud:
            board2[i][j] = board2[i][j-1] + 1

    cloud = False

for i in range(H):
    print(*board2[i])



