# 마구간 정하기(결정 알고리즘)
def Count(x):
    cnt = 1
    ep = x_arr[0]
    for i in range(1, len(x_arr)):
        if x_arr[i] - ep >= x:
            cnt += 1
            ep = x_arr[i]

    return cnt


N, C = map(int, input().split())
x_arr = [int(input()) for _ in range(N)]
x_arr.sort()
res = 0
lp = 1  # 두 마구간의 거리는 최소 1
rp = x_arr[N-1]  # 마지막 마구간까지의 거리
while lp <= rp:
    md = (lp + rp) // 2
    if Count(md) >= C:
        res = md
        lp = md + 1
    else:
        rp = md - 1

print(res)
