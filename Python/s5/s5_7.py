# 교육과정 설계
from collections import deque

data = input()
for tc in range(int(input())):
    idx = 0
    res = False
    q = deque(list(map(str, input())))
    while q:
        sub = q.popleft()
        if data[idx] == sub:
            idx += 1
        elif sub in data[idx+1:]:
            break

        if idx > len(data)-1:
            res = True
            break
    if res:
        print("#%d YES" % (tc + 1))
    else:
        print("#%d NO" % (tc+1))
