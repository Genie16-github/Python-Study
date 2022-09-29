# [G4]좋다
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
res = 0

for k in range(n):
    num = data[k]  # 서로 다른 수 두 개의 합
    i = 0  # 시작 idx
    j = n-1  # 끝 idx
    while i < j:
        if data[i] + data[j] == num:  # 정답
            if i != k and j != k:
                res += 1
                break   # 굳이 다 확인해 볼 필요가 없음
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif data[i] + data[j] < num:
            i += 1
        else:
            j -= 1

print(res)