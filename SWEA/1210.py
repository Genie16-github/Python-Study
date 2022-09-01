# 1210. Ladder1
dy = [0, 1, -1]  # 위, 오른쪽, 왼쪽
dx = [-1, 0, 0]

for _ in range(10):
    t = int(input())
    data = list([0] + list(map(int, input().split())) + [0] for _ in range(100))
    visited = [[0] * 102 for _ in range(100)]
    x, y = 99, data[99].index(2)  # 도착점 - 출발점을 찾기 위해 도착점부터 거꾸로
    visited[x][y] == 1

    while True:
        if x == 0:   # x 좌표가 0이면 출발점에 도착했기 때문에 탈출
            break

        if data[x][y+1] == 1 and visited[x][y+1] == 0:  # 오른쪽에 1이 있을 때
            y += dy[1]
            x += dx[1]
            visited[x][y] = 1

        elif data[x][y-1] == 1 and visited[x][y-1] == 0:  # 왼쪽에 1이 있을 때
            y += dy[2]
            x += dx[2]
            visited[x][y] = 1

        else:  # 위쪽에 1이 있을 때
            y += dy[0]
            x += dx[0]
            visited[x][y] = 1

    print('#{} {}'.format(t, y-1))
