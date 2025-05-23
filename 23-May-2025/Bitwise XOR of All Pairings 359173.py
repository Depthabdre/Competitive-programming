# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        total = 0
        nums2xor = 0
        for num in nums2:
            nums2xor ^= num
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0
        elif len(nums2) % 2 == 0:
            return nums2xor
        else:
            ans = 0
            temp =  nums2xor
            for num in nums1:
                ans ^= num
                ans ^= temp
            return ans
        return 0



        