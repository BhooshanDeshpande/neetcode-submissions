class Solution:
    def rob(self, nums: List[int]) -> int:

        prev2 = 0
        prev = 0

        for i in nums:
            curr = max(prev2+i, prev)
            prev2 = prev 
            prev = curr
        
        return max(curr, prev)
        


