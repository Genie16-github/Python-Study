# 침몰하는 타이타닉(그리디)
from collections import deque

N, M = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort(reverse=True)
weights = deque(weights)
cnt = 0
while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] > M:
        cnt += 1
        weights.popleft()
    else:
        cnt += 1
        weights.popleft()
        weights.pop()

print(cnt)
