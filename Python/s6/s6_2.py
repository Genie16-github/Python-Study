# 이진트리 순회(깊이우선탐색)
def dfs(v):
    if v > 7:
        return
    else:
        print(v, end=' ')  # 전위순회(대표적)
        dfs(v*2)
        # print(v, end=' ')  # 중위순회
        dfs(v*2+1)
        # print(v, end=' ')  # 후위순회 ex)병합정렬


if __name__ == "__main__":
    dfs(1)
