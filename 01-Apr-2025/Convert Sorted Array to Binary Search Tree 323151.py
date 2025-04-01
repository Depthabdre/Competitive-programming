# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def divideconquer(arr):
            if len(arr) == 1:
                return TreeNode(arr[0])
            elif len(arr) == 0:
                return None
            mid = len(arr) // 2
            left = divideconquer(arr[:mid])
            right = divideconquer(arr[mid + 1 : ])

            root = TreeNode(arr[mid])
            root.left = left
            root.right = right
            return root
        return divideconquer(nums)
        