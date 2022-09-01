import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())

second = (c + d) % 60
tmp = (c + d) // 60
minute = (b + tmp) % 60
tmp = (b + tmp) // 60
hour = (a + tmp) % 24

print(hour, minute, second)
