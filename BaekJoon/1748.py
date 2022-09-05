# [S4]수 이어 쓰기1
import sys
input = sys.stdin.readline

num = ''
n = int(input())
for i in range(1, n+1):
    num += ''.join(str(i))

print(len(num))