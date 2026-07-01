class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}
        for i in range(len(nums)):
            if nums[i] not in position:
                position[nums[i]] = i
        
        ind1 = None
        ind2 = None
        for i in range(len(nums)): 
            c = target - nums[i]
            if c in position and position[c] != i:
                ind1 = position[c]
                ind2 = i
                break
        
        if not (ind1 or ind2):
            raise ("Complement doesn't exist")
        
        return sorted([ind1, ind2])
        


