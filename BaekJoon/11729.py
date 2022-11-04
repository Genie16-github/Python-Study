# [S1]하노이 탑 이동 순서
import sys
input = sys.stdin.readline


def top(n, start, end):
    if n == 1:
        print(start, end)
        return

    top(n - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    top(n - 1, 6 - start - end, end)  # 3단계


N = int(input())
print(2 ** N - 1)
top(N, 1, 3)
