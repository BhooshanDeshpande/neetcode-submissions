import heapq
import math
class Solution:



    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []
        def find_dist(x1, y1):
            return math.sqrt((x1)**2 + (y1)**2)

        for i in points: 
            x, y = i[0], i[1]
            dst = find_dist(x, y)
            heapq.heappush(dist_heap, (dst, i))

        closest_points = []
        
        for i in range(k):
            x, y = heapq.heappop(dist_heap)[1]
            closest_points.append([x,y])

        return closest_points