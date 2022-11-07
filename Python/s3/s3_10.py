# 스토쿠 검사
def check(graph):
    for i in range(9):
        ch1 = [0] * 10  # 각 행의 합 체크
        ch2 = [0] * 10  # 각 열의 합 체크
        for j in range(9):
            ch1[graph[i][j]] = 1
            ch2[graph[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:  # 행이나 열의 합이 9가 아니면
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10  # 그룹 체크
            for k in range(3):  # 그룹 안에 행
                for s in range(3):  # 그룹 안에 열
                    ch3[graph[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


Sudoku = [list(map(int, input().split())) for _ in range(9)]
if check(Sudoku):
    print("YES")
else:
    print("NO")
