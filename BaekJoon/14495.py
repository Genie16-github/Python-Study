# [S4]피보나치 비스무리한 수열
n = int(input())
arr = [1] * 116

for i in range(3, n):
    arr[i] = arr[i-3] + arr[i-1]
print(arr[n - 1])
