# 알파코드
import sys
input = sys.stdin.readline


def dfs(v, p):
    global cnt
    if v == n:
        cnt += 1
        for x in range(p):
            print(chr(res[x]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if data[v] == i:
                res[p] = i
                dfs(v+1, p+1)
            elif i >= 10 and data[v] == i // 10 and data[v+1] == i % 10:
                res[p] = i
                dfs(v+2, p+1)


if __name__ == "__main__":
    data = list(map(int, input().rstrip()))
    n = len(data)
    data.append(-1)
    res = [0]*(n+3)
    cnt = 0
    dfs(0, 0)
    print(cnt)
