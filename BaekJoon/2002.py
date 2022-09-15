# [S1]추월
import sys
input = sys.stdin.readline

n = int(input())

in_data = [input().rstrip() for _ in range(n)]
cnt = 0

for _ in range(n):
    num = input().rstrip()
    if in_data[0] != num:
        cnt += 1
    in_data.remove(num)
print(cnt)
