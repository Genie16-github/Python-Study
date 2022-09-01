import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = []
score = [0] * n
result = []

for _ in range(n):
    arr = list(map(int, input().split()))
    card.append(arr)

for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(card[j][i])
    max1 = max(tmp)
    for j in range(n):
        if max1 == tmp[j]:
            score[j] += 1
winner = max(score)

for i in range(n):
    if score[i] == winner:
        result.append(i+1)

print(result)
