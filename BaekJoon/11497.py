# [S1]통나무 건너뛰기
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    res = 0
    for i in range(n-2):
        res = max(res, abs(data[i] - data[i+2]))

    print(res)