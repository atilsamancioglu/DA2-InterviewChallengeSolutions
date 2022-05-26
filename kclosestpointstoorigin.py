'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x,y in points:
            distanceToOrigin = (x**2) + (y**2) #do not have to take sqrt because we will compare anyway
            minHeap.append([distanceToOrigin,x,y]) #append distance as first element bc python will evaluate it by default when heapified
            
        heapq.heapify(minHeap)
        
        result = []
        
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
        
        return result