# [S1]신입 사원
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data = []
    top = 0
    cnt = 1
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))

    data.sort()

    for i in range(1, len(data)):
        if data[i][1] < data[top][1]:
            top = i
            cnt += 1

    print(cnt)
