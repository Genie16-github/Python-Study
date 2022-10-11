# [S2]아이들과 선물 상자
import heapq
import sys
input = sys.stdin.readline

res = True
q = []
n, m = map(int, input().split())
tmp = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(q, (-tmp[i], tmp[i]))
w = list(map(int, input().split()))

for j in range(len(w)):
    a = heapq.heappop(q)[1]
    if a >= w[j]:
        heapq.heappush(q, (-(a-w[j]), a-w[j]))
    else:
        res = False
        break

print(1) if res else print(0)