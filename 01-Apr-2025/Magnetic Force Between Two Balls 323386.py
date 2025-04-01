# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        len_position = len(position)

        def checker(value):
            prev = position[0]
            count = 1  
            for i in range(1, len_position):
                if position[i] - prev >= value:
                    prev = position[i]
                    count += 1
                    if count >= m: 
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        ans = 1

        while left <= right: 
            mid = left + (right - left) // 2
            if checker(mid):
                ans = mid  
                left = mid + 1  
            else:
                right = mid - 1  
        
        return ans
