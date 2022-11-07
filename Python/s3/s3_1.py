# 회문 문자열 검사
import sys
input = sys.stdin.readline

N = int(input())
for t in range(N):
    data = str(input().strip()).upper()
    if data == data[::-1]:
        print("#%d YES" % (t+1))
    else:
        print("#%d NO" % (t+1))


"""
    # 직접 비교하는 코드를 작성해보는게 중요!
    for i in range(len(data)//2):
        if data[i] != data[-1-i]:
            print("#%d NO" % (t+1))
            break
    else:
        print("#%d YES" % (t+1))
"""

