class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2 

        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                elif prod > 2520 * g:
                    break

        return ans