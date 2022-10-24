# [B2]ACM 호텔
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(str(h) + format((n // h), '02'))
    else:
        print(str((n % h)) + format((n // h) + 1, '02'))

