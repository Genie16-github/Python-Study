# SWEA 1954. 달팽이 숫자
dy = [1, 0, -1, 0]  # 우, 하, 좌, 상
dx = [0, 1, 0, -1]  # 해당 사이클 반복

for t in range(int(input())):
    n = int(input())
    data = [[0] * n for _ in range(n)]   # n * n

    x, y = 0, 0
    cnt = 1
    data[x][y] = cnt  # 시작점
    dir = 0

    while True:
        if cnt == n**2:
            break

        a = x + dx[dir]
        b = y + dy[dir]

        if 0 <= a < n and 0 <= b < n and not data[a][b]:  # 범위를 초과하지 않고 값이 0이면 수행
            cnt += 1
            data[a][b] = cnt
            x, y = a, b  # 좌표 갱신. 현 위치 기억
        else:
            dir = (dir+1) % 4   # 방향 전환

    print('#{0}'.format(t+1))
    for i in range(n):
        print(*data[i])


