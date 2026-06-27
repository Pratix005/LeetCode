class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 0
        
        if 1 in count:
            c1 = count[1]
            max_len = c1 if c1 % 2 != 0 else c1 - 1
            
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            current = x
            while count[current] >= 2:
                current_len += 2
                current = current * current
            if count[current] >= 1:
                current_len += 1
            else:
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len