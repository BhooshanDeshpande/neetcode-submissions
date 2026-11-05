class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, x in enumerate(nums):
            if not target-x in comp:
                comp[target-x] = i 
        
        for i, x in enumerate(nums):
            if x in comp:
                if i == comp[x]:
                    continue
                return sorted([i, comp[x]])




        return []