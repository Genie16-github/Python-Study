# 수들의 합
N, M = map(int, input().split())
nums = list(map(int, input().split()))

lp, rp = 0, 1
tot = nums[0]
cnt = 0

while True:
    if tot < M:
        if rp < N:
            tot += nums[rp]
            rp += 1
        else:
            break
    elif tot == M:
        cnt += 1
        tot -= nums[lp]
        lp += 1
    else:
        tot -= nums[lp]
        lp += 1

print(cnt)


"""
# 시간 초과
lp, rp = 0, 1
cnt = 0

while lp < N and rp < N:
    total = 0
    for i in range(lp, rp+1):
        total += nums[i]

    if total < M:
        rp += 1
    elif total == M:
        cnt += 1
        lp += 1
    else:
        lp += 1

print(cnt)
"""