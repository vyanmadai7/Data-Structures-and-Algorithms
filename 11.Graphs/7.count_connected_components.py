def count_components(adj, n):
    vis = [False] * n

    def dfs(u):
        vis[u] = True
        for v, _ in adj[u]:
            if not vis[v]:
                dfs(v)

    cnt = 0
    for i in range(n):
        if not vis[i]:
            cnt += 1
            dfs(i)

    return cnt