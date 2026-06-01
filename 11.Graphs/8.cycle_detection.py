def has_cycle_undirected(adj, n):
    vis = [False] * n

    def dfs(u, p):
        vis[u] = True
        for v, _ in adj[u]:
            if not vis[v]:
                if dfs(v, u):
                    return True
            elif v != p:
                return True
        return False

    for i in range(n):
        if not vis[i]:
            if dfs(i, -1):
                return True
    return False