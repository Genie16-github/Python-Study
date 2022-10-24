# [S5]소수
import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
num = []

for i in range(m, n+1):
    cnt = 0
    for j in range(2, n+1):
        if i % j == 0:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        num.append(i)

if not num:
    print(-1)
else:
    print(sum(num))
    print(min(num))