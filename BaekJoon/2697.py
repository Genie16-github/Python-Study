# [S2]다음수 구하기
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, list(input().rstrip())))
    length, idx = len(data), 0
    for i in range(length-1, 0, -1):
        if data[i] > data[i-1]:
            if i == length - 1:
                idx = length - 2
            else:
                idx = i - 1
            break

    a = data[:idx]
    b = data[idx:]

    if not a or not b:
        print('BIGGEST')
    else:
        b.sort()
        for i in range(len(b)):
            if b[i] > data[idx]:
                a.append(b.pop(i))
                a.extend(b)
                break

        print(''.join(map(str, a)))