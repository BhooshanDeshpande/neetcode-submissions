class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [3,4,5,6,1,2]--case 1
        [1,2,3,4,5,6]--case 2

        lptr 0
        rptr 1
        lptrval 1  
        rptrval 3
        midptr 1
        midval 2
        '''

        lptr = 0
        rptr = len(nums) - 1

        while lptr < rptr:          
            lptrval = nums[lptr]
            rptrval = nums[rptr]

            if abs(lptr-rptr) == 1:
                x = lptrval if lptrval < rptrval else rptrval
                return x 

            midptr = lptr + (rptr-lptr)//2 # floors the int if diff is odd
            midval = nums[midptr] 

            if midval > rptrval: 
                # min is towards right
                lptr = midptr
            else: 
                rptr = midptr
        

        return nums[lptr]
        