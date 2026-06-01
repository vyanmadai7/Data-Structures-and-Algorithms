def dfs(adj, src, n):
    vis = [False] * n
    res = []

    def go(u):
        vis[u] = True
        res.append(u)
        for v, _ in adj[u]:
            if not vis[v]:
                go(v)

    go(src)
    return res