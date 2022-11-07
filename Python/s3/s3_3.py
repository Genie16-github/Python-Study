# 카드 역배치
card = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b+1-a)//2):
        card[a+i], card[b-i] = card[b-i], card[a+i]

print(*card[1::])