# [G5]행복 유치원
n, k = map(int, input().split())
data = list(map(int, input().split()))

dif = []
for i in range(1, n):
    dif.append(data[i] - data[i-1])

dif.sort()
print(sum(dif[:n-k]))
