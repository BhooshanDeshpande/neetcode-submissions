class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # brute force 
        # for i in nums: 
        #     if i in nums[i+1:]: 
        #         return False
        # return True
    
        # hashmap
        dct = {}
        for i in nums:
            if i in dct:
                return True
            else:
                dct[i] = True
        return False