# [D2]백만 장자 프로젝트
# 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 판매는 얼마든지 가능


def hoarding(price, start_idx):
    max_price = price[start_idx]  # 초기 max값 시작 포인트
    max_idx = start_idx
    total = 0

    for i in range(start_idx, len(price)):
        if price[i] > max_price:
            max_price = price[i]
            max_idx = i

    for i in range(start_idx, max_idx):
        total += max_price - price[i]

    if start_idx == len(price)-1:
        return 0

    if max_idx == start_idx:
        return hoarding(price, max_idx+1)
    return hoarding(price, max_idx) + total


T = int(input())
for i in range(1, T+1):
    n = int(input())
    p = list(map(int, input().split()))
    res = hoarding(p, 0)
    print("#{} {}".format(i, res))
