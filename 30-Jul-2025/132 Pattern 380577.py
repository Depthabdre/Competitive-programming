# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')
        
        # Traverse from right to left
        for num in reversed(nums):
            # If current number is less than 'third', pattern found
            if num < third:
                return True
            
            # While current number is greater than stack top, update 'third'
            while stack and num > stack[-1]:
                third = stack.pop()
            
            # Push current number as potential '3' in pattern
            stack.append(num)
        
        return False
