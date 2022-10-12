# [S1]센티와 마법의 뿅망치
import heapq
import sys
input = sys.stdin.readline

n, h, c = map(int, input().split())
gh = []
for i in range(n):
    height = int(input())
    heapq.heappush(gh, (-height, height))

cnt = 0
for i in range(c):
    a = heapq.heappop(gh)[1]
    if a < h:
        heapq.heappush(gh, (-a, a))
        break
    elif a == 1:
        heapq.heappush(gh, (-a, a))
    else:
        a = a // 2
        heapq.heappush(gh, (-a, a))
        cnt += 1

if gh[0][1] < h:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(heapq.heappop(gh)[1])