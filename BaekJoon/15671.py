# [S1]오셀로
n = int(input())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(stone, i, j, d):
    nx, ny = i + dx[d], j + dy[d]
    if not (0 <= nx < 6 and 0 <= ny < 6) or mat[nx][ny] == '.':
        return False
    if mat[nx][ny] == stone:
        return True
    if dfs(stone, nx, ny, d):
        mat[nx][ny] = stone
        return True
    return False


mat = [["."] * 6 for _ in range(6)]
mat[2][2], mat[3][3] = 'W', 'W'
mat[2][3], mat[3][2] = 'B', 'B'
for i in range(n):
    r, c = map(int, input().split())
    for d in range(8):
        mat[r-1][c-1] = "W" if i % 2 else "B"
        dfs("W" if i % 2 else "B", r-1, c-1, d)

for a in mat:
    print("".join(map(str, a)))
cnt = 0
for i in range(6):
    for j in range(6):
        if mat[i][j] == 'W':
            cnt += 1
        if mat[i][j] == 'B':
            cnt -= 1

print("White" if cnt > 0 else "Black")
