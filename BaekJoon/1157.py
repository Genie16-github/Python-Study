# [B1]단어 공부
data = input().upper()
set_data = list(set(data))  # 중복 제거

cnt_list = []

for i in set_data:
    cnt = data.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:  # 개수가 가장 많은 문자의 수가 2이상일 때
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(set_data[max_index])
