# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def can_split(max_sum):
            splits, curr = 1, 0
            for num in nums:
                if curr + num > max_sum:
                    splits += 1
                    curr = num
                    if splits > k:
                        return False
                else:
                    curr += num
            return True

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
