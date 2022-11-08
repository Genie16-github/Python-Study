# 뮤직비디오(결정 알고리즘)
def Count(x):
    total = 0
    cnt = 1
    for i in range(len(music)):
        total += music[i]
        if total > x:
            cnt += 1
            total = music[i]

    return cnt


N, M = map(int, input().split())
music = list(map(int, input().split()))

lp = 1
rp = sum(music)
res = 0
while lp <= rp:
    md = (lp + rp) // 2
    if md >= max(music) and Count(md) <= M:
        rp = md - 1
        res = md
    else:
        lp = md + 1

print(res)
