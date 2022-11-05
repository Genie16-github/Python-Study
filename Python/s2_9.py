# 주사위 게임
import sys
input = sys.stdin.readline

max_money = 0
N = int(input())
for i in range(N):
    cnt = [0] * 7
    for j in map(int, input().split()):
        cnt[j] += 1

    tmp = 0
    for idx, x in enumerate(cnt):
        if x == 3:
            tmp = 10000 + idx * 1000
        elif x == 2:
            tmp = 1000 + idx * 100
        elif x == 1:
            if tmp < idx * 100:
                tmp = idx * 100

    if tmp > max_money:
        max_money = tmp

print(max_money)

