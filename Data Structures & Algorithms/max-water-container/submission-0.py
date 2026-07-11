class Solution:
    def maxArea(self, heights: List[int]) -> int:

        lptr = 0
        rptr = len(heights)-1

        maxArea = float('-inf')
        while lptr < rptr:
            w = rptr - lptr 
            h = heights[lptr] if heights[lptr] < heights[rptr] else heights[rptr]
            curr_maxArea = w*h
            if curr_maxArea > maxArea:
                maxArea = curr_maxArea
            
            if heights[rptr] < heights[lptr]:
                rptr -= 1
            else:
                lptr += 1
        
        return maxArea

        '''
        lptr 1
        rptr 7
        maxArea 36 
        '''
        