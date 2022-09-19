# [S2]차이를 최대로
import sys
input = sys.stdin.readline

def permu(list_a):
    k = -1
    m = -1

    for i in range(len(list_a) - 1):
        if list_a[i] < list_a[i + 1]:
            k = i

    if k == -1:
        return [-1]

    for i in range(k, len(list_a)):
        if list_a[k] < list_a[i]:
            m = i

    list_a[k], list_a[m] = list_a[m], list_a[k]
    list_a = list_a[:k + 1] + sorted(list_a[k + 1:])
    return list_a


n = int(input())
data = list(map(int, input().split()))
data.sort()

ans = 0
s = 0
for j in range(len(data) - 1):
    s += abs(data[j] - data[j + 1])
if s > ans:
    ans = s

arr = data

while True:
    arr = permu(arr)
    if arr == [-1]:
        break
    s = 0

    for j in range(len(arr) - 1):
        s += abs(arr[j] - arr[j + 1])
    if s > ans:
        ans = s

print(ans)