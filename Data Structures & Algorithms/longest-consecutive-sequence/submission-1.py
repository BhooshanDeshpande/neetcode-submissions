class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # check starts
        max_len = 0
        for i in nums_set: 
            if i-1 not in nums_set:
                curr_len = 1
                nxt = i+1
                while nxt in nums_set:
                    curr_len += 1
                    nxt = nxt + 1
                if curr_len > max_len:
                    max_len = curr_len
                            
        return max_len
        