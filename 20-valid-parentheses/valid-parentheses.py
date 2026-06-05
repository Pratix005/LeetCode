class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        stack=[]

        for boo in s:
            if boo in map:
                top_ele = stack.pop() if stack else '#'

                if map[boo] != top_ele:
                    return False
            else:
                stack.append(boo)
        return len(stack) == 0
        