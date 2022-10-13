# [B2]벌집
import sys
input = sys.stdin.readline

n = int(input())
num = 1
cnt = 1
if n == 1:
    print(cnt)
else:
    while n > num:
        num += 6*cnt
        cnt += 1

    print(cnt)