# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        def optimal_founder(house_position):
            left = 0
            right = len(heaters)
            
           
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] >= house_position:
                    right = mid
                else:
                    left = mid + 1

            best = float('inf')
            
            if left < len(heaters):
                best = min(best, abs(heaters[left] - house_position))
            
            if left > 0:
                best = min(best, abs(heaters[left - 1] - house_position))
            
            return best

        answer = 0
        for x in houses:
            answer = max(answer ,optimal_founder(x))
        
        return answer
            


        