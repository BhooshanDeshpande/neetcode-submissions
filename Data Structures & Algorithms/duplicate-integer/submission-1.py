from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = defaultdict(lambda: 0)

        for i in nums:
            duplicate[i] += 1
            if duplicate[i] > 1: 
                return True

        return False
        