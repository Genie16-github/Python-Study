# [S4]스위치 켜고 끄기
def OnOff(num):
    if data[num] == 1:
        data[num] = 0
    else:
        data[num] = 1

n = int(input())
data = list(map(int, input().split()))
data = [0] + data

for _ in range(int(input())):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num, len(data), num):
            OnOff(i)
    else:
        OnOff(num)
        for i in range(n//2):
            if num - i < 1 or num + i > n:
                break

            if data[num - i] != data[num + i]:
                break
            else:
                OnOff(num - i)
                OnOff(num + i)

for i in range(1, len(data)):
    print(data[i], end=" ")
    if i % 20 == 0:
        print()