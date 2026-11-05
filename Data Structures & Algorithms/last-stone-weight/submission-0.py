import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_maxheap = []
        for i in stones:
            heapq.heappush(stones_maxheap, -i)

        while len(stones_maxheap) >= 2: 
            stone1 = -1*heapq.heappop(stones_maxheap)
            stone2 = -1*heapq.heappop(stones_maxheap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(stones_maxheap, -stone1+stone2)
            else:
                heapq.heappush(stones_maxheap, -stone2+stone1)

        if len(stones_maxheap) == 1:
            return -1*stones_maxheap[0]
        else:
            return 0
        
            

        