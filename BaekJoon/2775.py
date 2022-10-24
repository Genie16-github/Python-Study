# [B1]부녀회장이 될테야
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())  # 층수
    n = int(input())  # 호수
    p = [i for i in range(1, n+1)]  # 0층 1호부터 n호까지 사람 수

    for x in range(k):
        for y in range(1, n):
            p[y] += p[y-1]

    print(p[-1])
