import sys
input = sys.stdin.readline

n = int(input())  # 과목 수
score = list(map(int, input().split()))
max_score = max(score)

res = []
for i in score:
    res.append(i/max_score * 100)
r_avg = sum(res)/n
print(r_avg)
