# [S1]회의실 배정
N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: [x[1], x[0]])
et = 0
cnt = 0
for i in range(len(time)):
    if time[i][0] >= et:
        cnt += 1
        et = time[i][1]

print(cnt)
