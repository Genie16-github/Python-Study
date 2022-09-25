# [G5]콘센트
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))
time.sort(reverse=True)
heap = []

for t in time:
    if len(heap) < m:
        heapq.heappush(heap, t)
    else:
        outcome = heapq.heappop(heap)
        heapq.heappush(heap, outcome + t)

print(max(heap))

