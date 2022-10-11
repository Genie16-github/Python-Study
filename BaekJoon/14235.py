# [S3]크리스마스 선물
import heapq
import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if not q:
            print(-1)
        else:
            print(heapq.heappop(q)[1])
    else:
        for i in range(1, a[0]+1):
            heapq.heappush(q, (-a[i], a[i]))

