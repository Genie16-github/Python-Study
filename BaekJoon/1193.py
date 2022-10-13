# [B1]분수 찾기
import sys
input = sys.stdin.readline

line = 0
num = 0
x = int(input())
while x > num:
    line += 1
    num += line

if line % 2 == 0:  # 짝수일 때
    top = line - (num - x)
    bottom = (num - x) + 1
else:  # 홀수일 때
    top = (num - x) + 1
    bottom = line - (num - x)

print("{0}/{1}".format(top, bottom))