class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOGN = n.bit_length() + 1
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        parent = [-1] * n
        bfs_order = [0]
        visited = [False] * n
        visited[0] = True
        
        head = 0
        while head < len(bfs_order):
            u = bfs_order[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    bfs_order.append(v)

        up[0][0] = 0
        for k in range(1, LOGN):
            for i in range(n):
                up[i][k] = up[up[i][k - 1]][k - 1]

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        stack = [(0, 0)]
        timer += 1
        tin[0] = timer

        while stack:
            u, idx = stack[-1]
            if idx < len(children[u]):
                stack[-1] = (u, idx + 1)
                child = children[u][idx]
                timer += 1
                tin[child] = timer
                stack.append((child, 0))
            else:
                tout[u] = timer
                stack.pop()

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOGN):
                if (diff >> k) & 1:
                    u = up[u][k]
            if u == v:
                return u
            for k in range(LOGN - 1, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]

        bit = [0] * (n + 2)

        def bit_xor(i: int, val: int) -> None:
            while i <= n:
                bit[i] ^= val
                i += i & (-i)

        def update_range(l: int, r: int, val: int) -> None:
            bit_xor(l, val)
            bit_xor(r + 1, val)

        def query_point(i: int) -> int:
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & (-i)
            return res

        char_vals = [1 << (ord(c) - 97) for c in s]
        for u in range(n):
            update_range(tin[u], tout[u], char_vals[u])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                new_val = 1 << (ord(new_c) - 97)
                delta = char_vals[u] ^ new_val
                if delta:
                    char_vals[u] = new_val
                    update_range(tin[u], tout[u], delta)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)

                path_mask = query_point(tin[u]) ^ query_point(tin[v]) ^ char_vals[lca]
                ans.append((path_mask == 0) or ((path_mask & (path_mask - 1)) == 0))

        return ans