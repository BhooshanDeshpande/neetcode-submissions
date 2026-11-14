class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        solution = []

        def backtrack(i):
            if i >= len(nums):
                result.append(solution.copy())
                return

            backtrack(i+1)

            solution.append(nums[i])
            backtrack(i+1)
            solution.pop()

        backtrack(0)
        return result
        