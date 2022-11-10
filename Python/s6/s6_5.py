# 바둑이 승차(DFS)
def dfs(idx, total, t_tot):
    global max_weights
    if total + (sum(weights)-t_tot) < max_weights or total > C:
        return
    if idx == N:
        if total > max_weights:
            max_weights = total
    else:
        dfs(idx+1, total + weights[idx], t_tot + weights[idx])
        dfs(idx+1, total, t_tot + weights[idx])


if __name__ == "__main__":
    C, N = map(int, input().split())
    weights = [int(input()) for _ in range(N)]
    max_weights = -2147000000
    dfs(0, 0, 0)
    print(max_weights)