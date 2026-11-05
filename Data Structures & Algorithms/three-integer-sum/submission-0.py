class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans_pair = []
        print(nums)
        for i, x in enumerate(nums):
            lp = 0
            rp = len(nums)-1
            while lp < rp:
                if lp == i:
                    lp+=1
                    continue
                elif rp == i:
                    rp-=1
                    continue
                else:
                    balance = 0 - x
                    curr_sum = nums[lp] + nums[rp]
                    if curr_sum < balance:
                        lp += 1
                    elif curr_sum > balance:
                        rp -= 1
                    else:
                        pair = sorted([x, nums[lp], nums[rp]])
                        print(pair)
                        if pair not in ans_pair:
                            ans_pair.append(pair)
                        lp += 1
                    
        return ans_pair