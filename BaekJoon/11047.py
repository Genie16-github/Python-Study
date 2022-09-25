# [S4]동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
cnt = 0

for num in range(n, 0, -1):
    if k >= data[num-1]:
        cnt += k // data[num-1]
        k %= data[num-1]
    if k == 0:
        break

print(cnt)