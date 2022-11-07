# 회문
def check(string):
    lp = 0
    rp = len(string) - 1
    while lp < rp:
        if string[lp] == string [rp]:
            lp += 1
            rp -= 1
        else:
            if lp < rp - 1:
                tmp = string[:rp] + string[rp+1:]
                if tmp == tmp[::-1]:
                    return 1
            if lp + 1 < rp:
                tmp = string[:lp] + string[lp+1:]
                if tmp == tmp[::-1]:
                    return 1
            return 2

    return 0


N = int(input())
for _ in range(N):
    data = input()
    print(check(data))
