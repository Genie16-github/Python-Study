# [S5]소수 찾기
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    tmp = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            tmp += 1

    if tmp == 1:
        cnt += 1

print(cnt)
