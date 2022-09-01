# 1208. Flatten
for t in range(1, 11):  # 테스트 케이스 10개
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(n):  # 덤프 횟수만큼 수행
        data[data.index(max(data))] -= 1   # 최고 값을 찾아 -1
        data[data.index(min(data))] += 1   # 최소 값을 찾아 +1

    print('#{} {}'.format(t, max(data) - min(data)))
