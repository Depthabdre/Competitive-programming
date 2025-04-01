# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
       
        left, right = 1 , max(ranks) * cars * cars

        def canRepairInTime(mid):
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.sqrt(mid // rank)) 
                if total_cars >= cars:
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid 
            else:
                left = mid + 1 

        return left  
