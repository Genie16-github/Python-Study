# 응급실
from collections import deque

N, M = map(int, input().split())
q = deque([(x, idx) for idx, x in enumerate(list(map(int, input().split())))])
cnt = 0
while q:
    p = q.popleft()

    """
    # any -> 하나라도 참이면 실행
    if any(p[0] < x[0] for x in q):
        q.append(p)
    """

    for i in q:
        if p[0] < i[0]:
            q.append(p)
            break
    else:
        cnt += 1
        if p[1] == M:
            print(cnt)
            break



