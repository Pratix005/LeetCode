class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10**9 + 7

        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, parent):
            depth = 0

            for nei in g[node]:
                if nei != parent:
                    depth = max(depth, 1 + dfs(nei, node))

            return depth

        d = dfs(1, 0)

        return pow(2, d - 1, mod)