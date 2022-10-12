# [S5]셀프 넘버
import sys
input = sys.stdin.readline

num = [False] * 10000


def f_sum(x):
    total = x
    while x > 0:
        total += x % 10
        x //= 10

    if total < 10000 and not num[x]:
        num[total] = True


for i in range(1, 10000):
    f_sum(i)

for i in range(1, len(num)):
    if not num[i]:
        print(i)
