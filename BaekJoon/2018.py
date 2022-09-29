# [S4]수들의 합
import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
start_idx = 1
end_idx = 1
total = 1

while end_idx != n:
    if total == n:  # 정답 케이스
        cnt += 1
        end_idx += 1
        total += end_idx

    elif total > n:
        total -= start_idx
        start_idx += 1

    else:
        end_idx += 1
        total += end_idx

print(cnt)