# [S3]구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0]
tmp = 0

for i in arr:
    tmp += i
    arr_sum.append(tmp)

for i in range(m):
    a, b = map(int, input().split())
    print(arr_sum[b] - arr_sum[a-1])
