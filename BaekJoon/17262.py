# [S5]팬덤이 넘쳐흘러
import sys
input = sys.stdin.readline

n = int(input())  # 팬의 수
se = []
for _ in range(n):
    s, e = map(int, input().split())
    se.append((s, e))

max_value, min_value = 0, 10**6
for i in range(len(se)):
    max_value = max(max_value, se[i][0])  # 가장 늦게 등교
    min_value = min(min_value, se[i][1])  # 가장 빨리 하교

if max_value - min_value < 0:
    print(0)
else:
    print(max_value - min_value)
