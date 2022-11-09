# 최소힙
import heapq as hq

heap = []
while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, num)
