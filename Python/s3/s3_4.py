# 두 리스트 합치기
N = int(input())
nums_1 = list(map(int, input().split()))
M = int(input())
nums_2 = list(map(int, input().split()))

p1, p2 = 0, 0
res = []
while True:
    if p1 == N or p2 == M:
        break
    if nums_1[p1] < nums_2[p2]:
        res.append(nums_1[p1])
        p1 += 1
    else:
        res.append(nums_2[p2])
        p2 += 1

if p1 == N:
    res += nums_2[p2:]
else:
    res += nums_1[p1:]

print(*res)