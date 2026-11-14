class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted(nums)
        result = set()
        solution = []
        n = len(nums)
        def backtrack(i):
            curr_sum = sum(solution)
            if i >= n or curr_sum > target:
                return 

            if curr_sum == target:
                result.add(tuple(sorted((solution[:]))))
                return 

            solution.append(nums[i])
            backtrack(i)
            solution.pop()

            backtrack(i+1)

        
        backtrack(0)
        return [list(item) for item in result]
