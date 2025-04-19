# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length_num = len(nums)
        frequency_of_num = Counter(nums)
        frequency_of_num = dict(sorted(frequency_of_num.items(), key=lambda x: x[1], reverse=True))


        ans = []
        for key in frequency_of_num:
            if k > 0:
                ans.append(key)
                k-=1
        return ans
            
        