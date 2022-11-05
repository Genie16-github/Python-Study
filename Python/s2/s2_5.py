# 정다면체
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N&M : 4, 6, 8, 12, 20 중에 하나
cnt = [0] * (N+M+3)
max_sum = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1

res = []
for idx, x in enumerate(cnt):
    if x > max_sum:
        max_sum = x
        res = [idx]
    elif x == max_sum:
        res.append(idx)

print(*res)
