# [G5]두 배 더하기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0

while sum(data) != 0:
    check = 0
    for i in range(n):
        if data[i] % 2 != 0 or data[i] == 0 or data[i] == 1:
            if data[i] == 0:
                continue
            else:
                data[i] -=1
                cnt += 1
            check = 1
    if check == 0:
        for i in range(n):
            data[i] //= 2
        cnt += 1

print(cnt)