class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1
            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif ch == '#':
                lengths[i + 1] = cur * 2
            else:
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]
            cur = lengths[i]
            nxt = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == cur:
                    return ch

            elif ch == '*':
                if nxt < cur:
                    if k == nxt:
                        return "."

            elif ch == '#':
                half = cur
                k %= half

            else:  
                k = cur - 1 - k

        return "."