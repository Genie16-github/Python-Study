import math

t_score = 0
n = int(input())
for _ in range(n):
    score = input()
    tmp = ''
    for i in range(len(score)):
        if score[i] == '0' or score[i] == '6':
            tmp += '9'
        else:
            tmp += score[i]
    t_score += min(100, int(tmp))

ans = t_score / n
if ans - int(ans) >= 0.5:
    print(math.ceil(ans))
else:
    print(math.floor(ans))
