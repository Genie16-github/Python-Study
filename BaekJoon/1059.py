# [S4]좋은구간
L = int(input())
data = list(map(int, input().split()))
n = int(input())

data.append(0)
data.sort()

cnt = 0
for i in range(len(data)-1):
    if data[i] == n or data[i+1] == n:
        cnt = 0
        break
    elif (data[i] < n) and (n < data[i+1]):
        cnt = (n - data[i]) * (data[i+1] - n) - 1
        break

print(cnt)