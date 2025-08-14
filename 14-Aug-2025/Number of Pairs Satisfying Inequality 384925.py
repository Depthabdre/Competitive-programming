# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [a - b for a, b in zip(nums1, nums2)]
        n = len(arr)

        def merge_sort(l, r):
            if r - l <= 0:  # base case: one element
                return 0

            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)

            # Count valid pairs across halves
            j = mid + 1  # pointer in right half
            for i in range(l, mid + 1):
                # Move j until R[j] is large enough
                while j <= r and arr[j] < arr[i] - diff:
                    j += 1
                count += (r - j + 1)

            # Merge step — sort arr[l:r+1]
            temp = []
            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if arr[p1] <= arr[p2]:
                    temp.append(arr[p1])
                    p1 += 1
                else:
                    temp.append(arr[p2])
                    p2 += 1
            while p1 <= mid:
                temp.append(arr[p1])
                p1 += 1
            while p2 <= r:
                temp.append(arr[p2])
                p2 += 1
            arr[l:r+1] = temp

            return count

        return merge_sort(0, n - 1)
