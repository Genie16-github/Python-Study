# [G5]A와 B
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while len(t) != len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

print(1) if s == t else print(0)
