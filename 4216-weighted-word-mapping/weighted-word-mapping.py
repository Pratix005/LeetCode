class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for cha in word:
                total += weights[ord(cha) - ord('a')]

            ans.append(chr(ord('z') - (total % 26)))
        return ''.join(ans)