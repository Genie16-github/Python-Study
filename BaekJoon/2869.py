# [S5]달팽이는 올라가고 싶다
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
move, cnt = 0, 1
move += a
while move < v:
    move -= b
    cnt += 1
    move += a
print(cnt)