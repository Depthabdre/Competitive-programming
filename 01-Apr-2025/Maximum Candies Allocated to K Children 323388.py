# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left = 1
        right = sum(candies) // k
        while left <= right:
            mid = (left + right) // 2
            flag = False
            count = 0

            for candy in candies:
                count += candy // mid
                if k <= count:
                    flag = True

            if flag:
                left = mid + 1
            else:
                right = mid - 1
        
        return right