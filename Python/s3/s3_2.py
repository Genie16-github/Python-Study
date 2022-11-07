# 숫자만 추출
import sys
input = sys.stdin.readline

num = [str(i) for i in range(10)]
data = input().strip()
res = ''

for i in data:
    if i in num:
        res += i

res = int(res)
cnt = 1

for i in range(2, res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)

"""
data = input()
print(type(data))
res = 0
for x in data:
    if x.isdecimal():  # 0 ~ 9까지의 수
        res = res * 10 + int(x)
print(res)
"""