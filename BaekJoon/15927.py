# [G5]회문은 회문아니야!!
import sys
input = sys.stdin.readline

"""
# 시간초과 코드
data = input().strip()
cnt = len(data)

for i in range(len(data)-1, 0, -1):
    if data[:i+1:] != data[i::-1]:
        print(cnt)
        break
    else:
        cnt -= 1
else:
    print(-1)
"""

data = input().strip()
cnt = len(data)

if data == data[0] * cnt:
    print(-1)
elif data == data[::-1]:
    print(cnt-1)
else:
    print(cnt)
