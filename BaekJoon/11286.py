# [S1]절댓값 힙
import heapq
import sys
input = sys.stdin.readline

nums = int(input())
heap = []

for _ in range(nums):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
