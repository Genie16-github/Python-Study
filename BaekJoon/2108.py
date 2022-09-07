# [S3]통계학
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

print(round(sum(data) / n))  # 산술평균(소수점 이하 첫째 자리에서 반올림)

data.sort()
print(data[n // 2])  # 중앙값

cnt = Counter(data).most_common()  # 최빈값 구하기
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:  # 최빈값 2개 이상
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(data) - min(data))  # 범위(max - min)
