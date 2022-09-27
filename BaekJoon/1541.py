# [S2]잃어버린 괄호
import sys
input = sys.stdin.readline

data = input().split('-')
res = 0

for i in data[0].split('+'):
    res += int(i)

for i in data[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)
