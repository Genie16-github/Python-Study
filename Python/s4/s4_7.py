# 창고 정리
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

for i in range(M):
    arr[0] += 1
    arr[N-1] -= 1
    arr.sort()

print(arr[N-1] - arr[0])