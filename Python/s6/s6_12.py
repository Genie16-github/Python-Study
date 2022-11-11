# 인접행렬
N, M = map(int, input().split())
board = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    board[a-1][b-1] = w

for x in board:
    print(*x)