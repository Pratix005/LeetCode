class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]

                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
        return longest