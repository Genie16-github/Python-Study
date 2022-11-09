# 증가수열 만들기(그리디)
N = int(input())
data = list(map(int, input().split()))
ep = 0
lp = 0
rp = N-1
res = ''
while lp <= rp:
    tmp = []
    if data[lp] > ep:
        tmp.append((data[lp], 'L'))
    if data[rp] > ep:
        tmp.append((data[rp], 'R'))

    if len(tmp) == 0:
        break

    tmp.sort()
    res += tmp[0][1]
    ep = tmp[0][0]

    if tmp[0][1] == 'L':
        lp += 1
    else:
        rp -= 1

print(len(res))
print(res)
