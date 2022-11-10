# 재귀함수를 이용한 이진수 출력
def binary(x):
    if x == 0:
        return
    else:
        binary(x // 2)
        print(x % 2, end='')


if __name__ == "__main__":
    N = int(input())
    binary(N)