# 최대힙
import heapq as hq

h = []
while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(hq.heappop(h)[1])
    else:
        hq.heappush(h, (-num, num))