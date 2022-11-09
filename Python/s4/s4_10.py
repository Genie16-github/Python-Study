# 역수열(그리디)
N = int(input())
arr = list(map(int, input().split()))
res = [0] * N
for i in range(N):
    for j in range(N):
        if arr[i] == 0 and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            arr[i] -= 1

for x in res:
    print(x, end=' ')


