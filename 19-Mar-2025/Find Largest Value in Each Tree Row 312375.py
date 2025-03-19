# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def Maxfinder(node,level):
            if not node:
                return
            if len(ans) == level:
                ans.append(node.val)
            else:
                ans[level] = max(ans[level] , node.val)
            Maxfinder(node.right,level + 1)
            Maxfinder(node.left , level + 1)
        
        Maxfinder(root,0)
        return ans