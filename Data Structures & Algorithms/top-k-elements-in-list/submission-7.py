class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force - count freq of each elem in a dict, sort dict by val. return top k keys. 
        since it involves sorting o(nlogn)

        o(n) -
        keep a dict of int freq. keep track of lowest freq in topk. If any number's freq > lowest freq in top k
        remove lowest freq number in top k and set this freq as the new lowest. return top k

        k = 2
        topk = (-1, 1)
        lf = 1
        lfelem = 4
        freq = {4:1, 1:1, -1:2, 2:1, }
        i = -1

        '''

        freq_count = {}
        for i in nums:
            if i not in freq_count:
                freq_count[i] = 1
            else:
                freq_count[i] += 1
        #create a list of lists, where index is [] is freq, value = num
        # for e.g. [[], [1], [0], []] means (1,0,0)
        buckets = [[] for i in range(len(nums)+1)]
        for val, freq in freq_count.items():
            buckets[freq].append(val)
        
        topk = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                topk.append(num)
                if len(topk) == k:
                    return topk
        
        return topk

            

        