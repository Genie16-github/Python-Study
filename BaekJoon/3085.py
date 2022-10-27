# [S2]사탕 게임
import sys
input = sys.stdin.readline


def check(arr):
    n = len(arr)
    res = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > res:
                res = cnt

        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > res:
                res = cnt

    return res


n = int(input())
arr = [list(input()) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            temp = check(arr)

            if temp > res:
                res = temp

            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            temp = check(arr)

            if temp > res:
                res = temp

            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(res)
