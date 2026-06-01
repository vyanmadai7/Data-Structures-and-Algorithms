from collections import deque, defaultdict

def topo_sort(n, edges):
    g = defaultdict(list)
    indeg = [0] * n

    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    res = []

    while q:
        u = q.popleft()
        res.append(u)

        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return res if len(res) == n else []