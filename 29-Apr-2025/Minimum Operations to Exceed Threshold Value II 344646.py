# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        min_operation = 0
        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            pop_ele = min(first , second) * 2 + max(first, second)
            heapq.heappush(nums , pop_ele)
            min_operation += 1
        return min_operation

        