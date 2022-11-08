# 랜선 자르기(결정 알고리즘)
N, K = map(int, input().split())
line = [int(input()) for _ in range(N)]

lp = 1
rp = max(line)
res = 0
while lp <= rp:
    md = (lp + rp) // 2
    cnt = 0
    for i in line:
        cnt += i // md
    if cnt >= K:
        res = md
        lp = md + 1
    else:
        rp = md - 1

print(res)