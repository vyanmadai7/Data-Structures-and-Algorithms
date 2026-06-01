from collections import deque

def bfs(adj, src, n):
    vis = [False] * n
    q = deque([src])
    vis[src] = True
    res = []

    while q:
        u = q.popleft()
        res.append(u)
        for v, _ in adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)

    return res