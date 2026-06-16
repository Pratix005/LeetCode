class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in s:
            if i.islower():
                result.append(i)
            elif i == '*':
                if len(result) != 0:
                    result.pop(-1)
            elif i == '#':
                result += result
            elif i == '%':
                result.reverse()
            else:
                print("no char")
        return ''.join(result)
        
            