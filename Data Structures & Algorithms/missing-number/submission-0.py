class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        summ = nums_len*(nums_len + 1)/2

        for i in nums:
            summ = summ - i 
        
        return int(summ)
        