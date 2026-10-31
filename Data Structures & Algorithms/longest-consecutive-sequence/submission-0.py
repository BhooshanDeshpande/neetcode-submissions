class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # check starts
        max_len = 0
        for i in nums_set: 
            if i-1 not in nums_set:
                seq = [i]
                nxt = i+1
                while nxt in nums_set:
                    seq.append(nxt)
                    nxt = nxt + 1
                if len(seq) > max_len:
                    max_len = len(seq)
                            
        return max_len
        