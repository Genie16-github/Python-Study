# [S3]소수 구하기
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
ch = [0] * (N+1)

for i in range(2, N+1):
    if ch[i] == 0:
        if i >= M:
            print(i)
        for j in range(i, N+1, i):
            ch[j] = 1

