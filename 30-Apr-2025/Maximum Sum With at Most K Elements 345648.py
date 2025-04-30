# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        nums= []
        heapq.heapify(nums)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ele = (-grid[i][j],i)
                heapq.heappush(nums,ele)
        max_sum = 0
        count_num = 0
        while count_num < k:
            ele , index = heapq.heappop(nums)
            if limits[index] > 0:
                max_sum += -ele
                limits[index] -= 1
                count_num += 1
        return max_sum


