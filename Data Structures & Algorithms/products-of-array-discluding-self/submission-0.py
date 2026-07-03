class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Get product for one but last and then calculate others
        '''
        prefix_sum = [None]*len(nums)
        suffix_sum = [None]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[i] = 1
            else:
                prefix_sum[i] = prefix_sum[i-1]*nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix_sum[i] = 1
            else:
                suffix_sum[i] = suffix_sum[i+1]*nums[i+1]

        res = [None] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix_sum[i] * suffix_sum[i]

        return res

        



        