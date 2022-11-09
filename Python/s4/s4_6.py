# 씨름 선수(그리디)
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(reverse=True)  # 내림차순 정렬

weight = 0
cnt = 0
for h, w in info:
    if w > weight:
        cnt += 1
        weight = w

print(cnt)
