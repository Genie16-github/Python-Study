# 뒤집어진 소수
def isPrime(x):  # 소수 판별
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    else:
        return True


def reverse(x):  # 숫자 뒤집기
    tmp = str(x)
    for i in ['3', '4', '7']:
        if i in tmp:
            return False

    tmp = tmp.replace('6', '*').replace('9', '6').replace('*', '9')
    res = tmp[::-1]
    res = int(res)
    return isPrime(res)  # 뒤집은 숫자 소수 판별


N = int(input())
if isPrime(N):
    if reverse(N):
        print("yes")
    else:
        print("no")
else:
    print("no")
