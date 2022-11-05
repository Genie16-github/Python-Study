# 점수 계산
import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
total, res = 0, 0

for i in score:
    if i == 1:
        total += 1
        res += total
    else:
        total = 0

print(res)
