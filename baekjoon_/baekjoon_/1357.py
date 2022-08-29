import sys
input = sys.stdin.readline

x, y = map(str, input().split())
tmp = str(int(x[::-1]) + int(y[::-1]))
print(int(tmp[::-1]))
