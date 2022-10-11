# [S5]국회의원 선거
import sys
input = sys.stdin.readline

n = int(input())
das = int(input())
arr = []
for _ in range(n-1):
    arr.append(int(input()))

arr.sort(reverse=True)
cnt = 0
if n == 1:
    print(0)
else:
    while arr[0] >= das:
        arr[0] -= 1
        das += 1
        cnt += 1
        arr.sort(reverse=True)

    print(cnt)
