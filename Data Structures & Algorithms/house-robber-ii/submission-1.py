class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[1], nums[0])

        pass1 = nums[0:-1]
        pass2 = nums[1:]
  
        max_of_pass = 0
        for pass_n in [pass1, pass2]:
            prev2, prev1 = 0, 0 
            for i in pass_n:
                curr = max(i + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            max_of_pass = max(max_of_pass, curr)
        
        return max_of_pass
        