# 대표값
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
# ave = round(sum(data) / N)  # python은 round_half_even 방식 : half일 때는 짝수쪽으로
ave = int((sum(data) / N) + 0.5)
min_diff = float('inf')
score, res = data[0], 0

for idx, x in enumerate(data):  # enumerate(list) : index, value(값)을 제공
    if abs(x-ave) < min_diff:
        min_diff = abs(x-ave)
        score = x
        res = idx
    elif abs(x-ave) == min_diff:
        if score < x:
            score = x
            res = idx

print("%d %d" % (ave, res+1))


"""
diff = float('inf')  # 무한한 값
res = []

for i in range(N):
    if abs(ave - data[i]) < diff:
        diff = abs(ave - data[i])

for i in range(N):
    if abs(ave - data[i]) == diff:
        res.append(data[i])

res.sort(reverse=True)  # 내림차순 정렬
print("%d %d" % (ave, data.index(res[0])+1))
"""