# 공주 구하기(큐)
from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    q.popleft()

    if len(q) == 1:
        print(q[0])
        q.popleft()

