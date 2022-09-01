import sys
input = sys.stdin.readline

while True:
    try:
        cnt = 0
        n, m = map(int, input().split())
        for i in range(n, m + 1):
            tmp = [0] * 10
            i = str(i)
            for j in i:
                tmp[int(j)] += 1
            p = 0
            for j in tmp:
                if j > 1:
                    p += 1
            if p == 0:
                cnt += 1
        print(cnt)
    except:
        break



