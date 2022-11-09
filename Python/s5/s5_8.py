# 단어 찾기
N = int(input())
word = [input() for _ in range(N)]
dic = {x: 0 for x in word}

for _ in range(N-1):
    tmp = input()
    dic[tmp] += 1

for x in dic.keys():
    if dic[x] == 0:
        print(x)
        break
