# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        count = 0
        total_sum = 0
        heightDif = []
        temp = 0
        heapq.heapify(heightDif)
        if ladders > 0:
            for i in range(len(heights) - 1):
                if heights[i] < heights[i+1]:
                    dif = abs(heights[i] - heights[i+1])
                    total_sum += dif
                    heapq.heappush(heightDif,dif)
                    count += 1

                temp += 1

                if count >= ladders:
                    break
            
        total_sum = 0
        i = temp
        print(i)
        while i < (len(heights) - 1):
            if heights[i] < heights[i+1]:
                dif = abs(heights[i] - heights[i+1])
                if heightDif and dif > heightDif[0]:
                    total_sum += heapq.heappop(heightDif)
                    heapq.heappush(heightDif,dif)
                else:
                    total_sum += dif
                print(total_sum)
                if total_sum > bricks:
                    break
            
                i += 1
            else:
                i += 1


        
        return i 