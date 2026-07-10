class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict.keys():
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1

        buck_lst = [[] for i in range(len(nums)+1)]
        for val, freq in freq_dict.items():
            buck_lst[freq].append(val)

        ans = []
        for i in range(len(buck_lst)-1, -1, -1):
            curr_lst = buck_lst[i]
            for i in curr_lst:
                ans.append(i)
                if len(ans) ==k :
                    return ans
            
        return ans