class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 2)
        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        ans = 0
        update(rank[0])

        for p in pref[1:]:
            ans += query(rank[p] - 1)
            update(rank[p])

        return ans