# [G3]캐슬 디펜스
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arr = []

castle_pos = [i for i in range(m)]
archer = tuple(combinations(castle_pos, 3))  # 궁수는 3명 -> nC3
answer = 0


def get_enemy_count():
    global arr
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1

    return cnt


def attack_enemy(archer_case_index):
    global arr
    remove_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for archer_pos in archer[archer_case_index]:
        pq = []  # [거리, x, y]를 우선순위 큐에 삽입

        for i in range(n - 1, -1, -1):
            for j in range(m):
                if arr[i][j] == 1:
                    diff = abs(n - i) + abs(archer_pos - j)
                    if diff <= d:
                        heapq.heappush(pq, [diff, j, i])

        if pq:
            _, x, y = heapq.heappop(pq)
            remove_list.append([y, x])

    for y, x in remove_list:
        if not attacked[y][x]:
            attacked[y][x] = True
            cnt += 1
            arr[y][x] = 0

    return cnt


def move_enemy():  # 턴이 끝나면 적이 아래로 한칸 이동
    global arr
    arr[-1] = [0 for _ in range(m)]

    for i in range(-1, -n, -1):
        arr[i] = arr[i - 1]

    arr[0] = [0 for _ in range(m)]


def simulation(archer_case_index):
    cnt = 0
    while get_enemy_count() != 0:
        cnt += attack_enemy(archer_case_index)
        move_enemy()

    return cnt


for i in range(len(archer)):
    arr = [[board[i][j] for j in range(m)] for i in range(n)]
    cnt = simulation(i)
    if answer < cnt:
        answer = cnt

print(answer)

