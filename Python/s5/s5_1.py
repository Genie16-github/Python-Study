num, M = map(int, input().split())
res = [str(num)[0]]
cnt = 0
for i in str(num)[1:]:
    while res and int(i) > int(res[-1]) and cnt < M:
        res.pop()
        cnt += 1

    res.append(i)

if cnt < M:
    for _ in range(M-cnt):
        res.pop()

print(''.join(res))
