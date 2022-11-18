# [모의 SW 역량테스트] 수영장
def dfs(v, total):
    global res
    if v >= 12:
        if total < res:
            res = total
        return
    else:
        dfs(v+1, total + tmp[v])
        dfs(v+3, total + t)


t = int(input())
for tc in range(1, t+1):
    d, m, t, y = map(int, input().split())
    plan = list(map(int, input().split()))
    res = y  # 1년 이용권 요금
    tmp = []
    for i in range(12):
        if plan[i] * d > m:
            tmp.append(m)
        else:
            tmp.append(plan[i]*d)
    dfs(0, 0)
    print("#%d %d" % (tc, res))