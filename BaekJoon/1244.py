# [S4]스위치 켜고 끄기
def OnOff(num):  # 스위치 조작 함수
    if data[num] == 1:
        data[num] = 0
    else:
        data[num] = 1

n = int(input())
data = list(map(int, input().split()))
data = [0] + data  # 스위치 번호 1번부터 시작

for _ in range(int(input())):
    sex, num = map(int, input().split())

    if sex == 1:  # 남자
        for i in range(num, len(data), num):
            OnOff(i)
    else:  # 여자
        OnOff(num)
        for i in range(n//2):  # 하나를 기준으로 양쪽으로 체크하기 때문에 최대 n//2번
            if num - i < 1 or num + i > n:
                break

            if data[num - i] != data[num + i]:  # 대칭되는 스위치의 값이 다르면 탈출
                break
            else:
                OnOff(num - i)
                OnOff(num + i)

for i in range(1, len(data)):
    print(data[i], end=" ")
    if i % 20 == 0:  # 20개 초과시 한줄 밑에 출력
        print()