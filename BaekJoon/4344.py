# 평균은 넘겠지
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    tmp = list(map(int, input().split()))
    avg = sum(tmp[1:]) / tmp[0]

    for score in tmp[1:]:
        if score > avg:
            cnt += 1
    res = cnt / tmp[0] * 100
    print(f'{res:.3f}%')
