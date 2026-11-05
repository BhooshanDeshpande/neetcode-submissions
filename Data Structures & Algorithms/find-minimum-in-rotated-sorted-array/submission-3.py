class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        "123456"
        "234561"
        "345612"
        "456123" *
        "561234"
        "612345"
        """

        if nums[0] < nums[-1]:
            return nums[0] # fastest

        l , r = 0 , len(nums) - 1
        while (r-l>1): 
            m = int((l+r)/2) #truncate down
            
            if nums[m] - nums[l] < 0: 
                # left is where we should move
                r = m
            elif nums[r] - nums[m] < 0: 
                # right is where we shoud move
                l = m 
        
        if (nums[l] < nums[r]): 
            return nums[l]
        else:
            return nums[r]

        

























        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     m = int((l+r)/2)

        #     if nums[l] > nums[m] and nums[l] > nums[r]: 
        #         l = m
        #         continue
        #     if nums[r] > nums[m] and nums[r] > nums[l]: 
        #         r = m
        #         continue
        #     if nums[m] > nums[l] and nums[m] > nums[r]: 
        #         l = m 
        #         continue

        # return nums[m]


        