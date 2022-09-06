# [S5]덩치
n = int(input())  # 사람 수
data = []

for _ in range(n):
    xy = list(map(int, input().split()))
    data.append(xy)

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
