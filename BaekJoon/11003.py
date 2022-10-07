# [G1]최솟값 찾기
from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
q = deque()
data = list(map(int, input().split()))

for i in range(n):
    while q and q[-1][0] > data[i]:
        q.pop()
    q.append((data[i], i))
    if q[0][1] <= i - l:
        q.popleft()
    print(q[0][0], end=' ')
