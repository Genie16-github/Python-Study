# [S4]체스판 다시 칠하기
n, m = map(int, input().split())
ori = []
count = []

for _ in range(n):
    ori.append(input())

for a in range(n-7):
    for b in range(m-7):
        idx1, idx2 = 0, 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if ori[i][j] != 'W':
                        idx1 += 1
                    if ori[i][j] != 'B':
                        idx2 += 1
                else:
                    if ori[i][j] != 'B':
                        idx1 += 1
                    if ori[i][j] != 'W':
                        idx2 += 1
        count.append(min(idx1, idx2))

print(min(count))
