# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            run_sum = 0
            count = 0
            for i in range(len(weights)):
                run_sum += weights[i]
                if run_sum > mid:
                    count += 1
                    run_sum = weights[i]
            count += 1
            if count > days:
                low = mid + 1
            elif count <= days:
                high = mid - 1
                ans = min(ans,mid)
        return ans

        