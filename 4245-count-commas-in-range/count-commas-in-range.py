class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        for i in range(1, n + 1):
            total_commas += f"{i:,}".count(',')
        return total_commas